import os

import boto3


def get_batch_client():
    boto3.set_stream_logger()
    return boto3.client('batch', region_name='ap-south-1')


def tag_job_multiple(job_arn: str, tags: dict[str]):
    if is_an_array_job():
        job_arn = extract_parent_job_arn_from_child_job_arn(job_arn, get_array_index_from_env())

    c = get_batch_client()
    c.tag_resource(resourceArn=job_arn, tags=tags)


def tag_job_single(job_arn: str, tag_key: str, tag_value: str):
    tag_job_multiple(job_arn, {
        tag_key: tag_value
    })


def tag_job(status: str, reason: str = None):
    job_id = get_job_id_from_env()
    job_arn = retrieve_job_arn_from_job_id(job_id)

    tags = {
        'job_status': status
    }
    if reason is not None:
        tags['job_status_reason'] = reason

    tag_job_multiple(job_arn, tags)


def tag_job_success():
    if is_an_array_job():
        return
    tag_job('SUCCESS')


def tag_job_failure(fail_reason):
    tag_job('FAILED', fail_reason)


def retrieve_job_arn_from_job_id(job_id: str):
    c = get_batch_client()
    response = c.describe_jobs(jobs=[job_id])

    if response['jobs'] and type(response['jobs']) == list and len(response['jobs']) == 1 and response['jobs'][0][
        'jobArn']:
        return response['jobs'][0]['jobArn']

    raise RuntimeError()


def extract_parent_job_arn_from_child_job_arn(child_job_arn, array_index):
    return child_job_arn[0: len(child_job_arn) - len(array_index) - 1]


def get_job_id_from_env():
    return os.environ['AWS_BATCH_JOB_ID']


def is_an_array_job():
    try:
        return os.environ['AWS_BATCH_JOB_ARRAY_INDEX'] is not None
    except KeyError:
        return False


def get_array_index_from_env():
    return os.environ['AWS_BATCH_JOB_ARRAY_INDEX']
