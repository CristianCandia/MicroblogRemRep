'''
Created on 14/04/2013

@author: cristian
'''
import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))
<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
=======

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cristian:usuario@localhost/app' #' + os.path.join(basedir, 'app2')
>>>>>>> refs/heads/Postgre
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
