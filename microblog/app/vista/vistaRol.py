'''
Created on 03/05/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g

"""Se importa el metodo rol_CrearForm para manipular el formulario"""
from app.forms import rol_CrearForm, asignar_Permisos

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerRol

c_rol = ControllerRol()

@app.route('/rol')
@login_required
def rol():
    return render_template("rol2.html", title = 'Administracion de Roles')

@app.route('/rol/rol_crear', methods = ['GET', 'POST'])
@login_required
def crearRol():
    form = rol_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_rol.regRol(nombre = form.nombre.data,
                            descripcion = form.descripcion.data)
    if resp == 'Exito':
        redirect(url_for('rol'))
    return render_template("rol_crear.html", title = 'Crear rol', form = form)

@app.route('/rol_listar')
@login_required
def rol_listar():
    rol = c_rol.traerRoles()  
    return render_template("rol_listar.html", title = 'Listado de roles', Rol = rol)

@app.route('/rol/rol_asignar_permisos' , methods=['GET', 'POST'])
@login_required
def asignarPermisos():
    form = asignar_Permisos()
    resp = None
    if form.validate_on_submit():
        resp = c_rol.asignarPermisos(form.id_rol.data, form.id_permiso.data)
    if resp == 'Exito':
        flash('Se ha hecho la asignacion')
        redirect(url_for('rol'))
    if resp != None:
        flash(resp)
    return render_template("rol_asignar_permisos.html",title = 'Asignar Permisos', form = form)



