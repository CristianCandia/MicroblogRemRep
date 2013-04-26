'''
Created on 25/04/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, usr_CrearForm
from app import app, db, lm
@app.route('/proyecto')
def proyecto():
    return 'Hello World!'