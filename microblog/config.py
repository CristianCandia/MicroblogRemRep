'''
Created on 14/04/2013

@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
'''
import os
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cristian:usuario@localhost/app' #' + os.path.join(basedir, 'app2')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

'''Configuracion del correo del sistema'''
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'sigmasystem21'
MAIL_PASSWORD = 'useruser'

# administrator list
ADMINS = ['carlifer.fernando@gmail.com']