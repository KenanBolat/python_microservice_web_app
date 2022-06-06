FROM python:3.9

LABEL maintainer='Kenan BOLAT'
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install -r /tmp/requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000