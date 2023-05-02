FROM python:3

COPY classes.py main.py Test.py TestDriver.py /app/

WORKDIR /app

ENTRYPOINT ["python", "main.py"]