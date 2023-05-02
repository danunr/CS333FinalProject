FROM python:3

COPY classes.py main.py Test.py TestDriver.py CS333Final-Image /home/deassa/CS333/CS333FinalProject/

WORKDIR /home/deassa/CS333/CS333FinalProject/S333FinalProject

ENTRYPOINT ["python", "main.py"]