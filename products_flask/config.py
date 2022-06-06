import os


class Config(object):
    HOST = "db-flask"
    USER = os.environ.get('POSTGRES_USER')
    DEVDB = os.environ.get('POSTGRES_DB')
    PASS = os.environ.get('POSTGRES_PASSWORD')
    DB_URI = os.environ.get('DB_URI')
    print(PASS)
