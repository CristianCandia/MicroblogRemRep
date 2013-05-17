'''
Created on 14/04/2013

@author: cristian
'''

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy #estoy en master
from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir
import forms
from flask_mail import Mail

mail = Mail()
app = Flask(__name__)
app.config.from_object('config')
mail.init_app(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

db = SQLAlchemy(app)

from app import views, models
from app.modelo import usuario
from app.vista import vistaProyecto, vistaUsuario, vistaFase, vistaRol, vistaPermiso

