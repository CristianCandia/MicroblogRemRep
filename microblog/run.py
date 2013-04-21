'''
Created on 14/04/2013
@author: cristian miguel
'''
#!usr/lib/python
from app import app
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
print SQLALCHEMY_MIGRATE_REPO
print SQLALCHEMY_DATABASE_URI
print "Hola mundo"
app.run(debug = True)