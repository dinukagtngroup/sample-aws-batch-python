FROM python:3.9.9-slim-buster
LABEL org.opencontainers.image.source=https://github.com/dinukagtngroup/sample-aws-batch-python
WORKDIR /src
COPY requirments.txt requirments.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY src .
CMD ["python","main.py"]