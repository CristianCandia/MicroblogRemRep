'''
Created on 14/04/2013

@author: cristian
'''
import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://cristian:useruser:@localhost' + os.path.join(basedir, 'app2.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')