'''
Created on 14/04/2013

@author: cristian
'''
from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

db = SQLAlchemy(app)

from app import views, models
from controlador import vistaProyecto