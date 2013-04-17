'''
Created on 14/04/2013

@author: cristian
'''
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
from app import views