import os

class Config(object):
    # CELERY_BROKER_URL='amqp://guest:guest@localhost:5672//'
    # CELERY_RESULT_BACKEND='amqp://guest:guest@localhost:5672//'
    CELERY_BROKER_URL='redis://redis:6379//'
    #CELERY_RESULT_BACKEND='redis://admin:mypass@redis:5672//'
    #SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@localhost:5432/test" #used locally
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@db:5432/test" #used Docker
    SQLALCHEMY_TRACK_MODIFICATIONS = False

