'''
Created on 14/04/2013
@author: cristian miguel
'''
#!usr/lib/python
from app import app
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

app.run(debug = True)