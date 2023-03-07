FROM python:alpine3.17
LABEL org.opencontainers.image.source=https://github.com/dinukagtngroup/sample-aws-batch-python
COPY src src
CMD ["python","src/main.py"]