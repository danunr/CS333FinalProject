FROM python:3

RUN pip install coverage
RUN pip install unittest

WORKDIR /usr/src/app

ENTRYPOINT ["python", "main.py"]

