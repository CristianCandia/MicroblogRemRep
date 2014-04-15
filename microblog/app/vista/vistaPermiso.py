'''
Created on 03/05/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g

"""Se importa el metodo permiso_CrearForm para manipular el formulario"""
from app.forms import permiso_CrearForm

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerPermiso

c_permiso = ControllerPermiso()

@app.route('/permiso')
@login_required
def permiso():
    return render_template("permiso.html", title = 'Administracion de Permisos')

@app.route('/permiso/permiso_crear', methods = ['GET', 'POST'])
@login_required
def crearPermiso():
    print "entro en submit"
    print "entro en submit"
    form = permiso_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_permiso.regPermiso(nombre = form.nombre.data,
                                    codigo = form.codigo.data)
    if resp == 'Exito':
        redirect(url_for('permiso'))
    return render_template("permiso_crear.html", title = 'Crear permiso', form = form)

@app.route('/permiso_listar')
@login_required
def permiso_listar():
    print "entro en submit"
    print "entro en submit"
    print "entro en submit"
    permiso = c_permiso.traerPermisos()  
    return render_template("permiso_listar.html", title = 'Listado de permisos', Permiso = permiso)