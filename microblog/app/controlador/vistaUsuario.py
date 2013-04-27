'''
Created on 26/04/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, usr_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))