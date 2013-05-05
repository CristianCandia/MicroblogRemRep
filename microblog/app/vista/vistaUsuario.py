'''
Created on 26/04/2013

@author: cristian
'''

from flask import render_template, flash, redirect, session, url_for, request, g
from app.forms import LoginForm, usr_CrearForm, asignar_Roles
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
        resp = c_usr.regUsuario(name = form.nomUsr.data, passWord = form.passWord.data, 
                                nombre = form.nombre.data, apellido = form.apellido.data,
                                telefono = form.telefono.data, ci = form.ci.data, e_mail = form.e_mail.data)
    if resp == 'Exito':
        redirect(url_for('usuario'))
    return render_template("usr_crear.html", title = 'Crear usuario', form = form)

@app.route('/usuario/usuario_asignar_roles' , methods=['GET', 'POST'])
@login_required
def asignarRoles():
    form = asignar_Roles()
    resp = None
    if form.validate_on_submit():
        resp = c_usr.asignarRoles(form.id_usr.data, form.id_rol.data)
    if resp == 'Exito':
        flash('Se ha hecho la asignacion')
        redirect(url_for('usuario'))
    if resp != None:
        flash(resp)
    return render_template("usr_asignar_roles.html",title = 'Asignar Roles', form = form)
