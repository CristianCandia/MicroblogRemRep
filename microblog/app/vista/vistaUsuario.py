'''
Created on 26/04/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, usr_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerUsr

c_usr = ControllerUsr()

@app.route('/usuario/crear_usr2', methods = ['GET', 'POST'])
@login_required
def crearUsuario():
    form = usr_CrearForm()
    resp = None
    if form.validate_on_submit():
        nombre = form.nomUsr.data
        passWord = form.passWord.data
        role = 1
        resp = c_usr.regUsuario(nombre, passWord, role)
    if resp == 'Exito':
        redirect(url_for('usuario'))
    return render_template("usr_listar.html", title = 'Añadir usuarios')