FROM python:3

USER root
WORKDIR /usr/src/app

COPY src src
COPY ./requirements.txt .
COPY ./database.ini .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /usr/src/app

ENTRYPOINT ["python", "./src/main.py"]

