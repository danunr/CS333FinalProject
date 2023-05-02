FROM python:3

COPY classes.py main.py Test.py TestDriver.py /usr/src/app/

WORKDIR /usr/src/app

ENTRYPOINT ["python", "main.py"]