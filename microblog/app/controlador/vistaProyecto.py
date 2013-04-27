'''
Created on 25/04/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, usr_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid




@app.route('/proyecto')
@login_required
def proyecto():
    return render_template("proyecto.html", title = 'Administracion de proyecto')