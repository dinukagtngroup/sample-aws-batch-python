FROM python:alpine3.17
LABEL org.opencontainers.image.source=https://github.com/dinukagtngroup/sample-aws-batch-python
WORKDIR /src
COPY requirements.txt requirments.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY src .
CMD ["python","main.py"]