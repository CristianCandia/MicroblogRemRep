'''
Created on 25/04/2013

@author: cristian
'''

from flask import render_template, flash, redirect, session, url_for, request, g
from app.forms import proy_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerProy

c_proy = ControllerProy()

@app.route('/proyecto')
@login_required
def proyecto():
    return render_template("proyecto.html", title = 'Administracion de proyecto')

@app.route('/proyecto/proy_crear', methods = ['GET', 'POST'])
@login_required
def crearProyecto():
    form = proy_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_proy.regProyecto(nombre = form.nomProy.data,
                                  descripcion = form.descripcion.data,
                                  fecha_de_creacion = form.fecha_creacion.data,
                                  complejidad_total = form.complejidad.data,
                                  estado = form.estado.data)
    if resp == 'Exito':
        redirect(url_for('proyecto'))
    return render_template("proy_crear.html", title = 'Crear rpoyecto', form = form)

@app.route('/proy_listar')
@login_required
def proy_listar():
    proy = c_proy.traerProyectos()  
    return render_template("proy_listar.html", title = 'Listado proyecto', Proyecto = proy)