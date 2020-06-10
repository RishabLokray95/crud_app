from flask import Flask, request
from BackEnd import config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from BackEnd import tasks



#Flask Server instance - flaskAppInstance
flaskAppInstance = Flask(__name__)

#Set Configurations
flaskAppInstance.config.from_object(config.Config)

#PostGre DataBase Instance/Migrations
db = SQLAlchemy(flaskAppInstance)
migrate = Migrate(flaskAppInstance, db)

celery = tasks.make_celery(flaskAppInstance)

#Cross Origin Resource Sharing
CORS(flaskAppInstance)