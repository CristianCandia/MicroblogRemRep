'''
Created on 03/05/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g

"""Se importa el metodo fase_CrearForm para manipular el formulario"""
from app.forms import fase_CrearForm

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerFase, ControllerProy

c_fase = ControllerFase()
c_proy = ControllerProy()

@app.route('/fase/')
@app.route('/fase/<idp>')
@login_required
def fase(idp = None):
    fases = c_proy.getFases(idp)
    nomProy = c_proy.getNombre(idp)
    return render_template("indexFase.html", title = 'Administracion de Fases', fases = fases, nomProy = nomProy)

@app.route('/fase/fase_crear', methods = ['GET', 'POST'])
@login_required
def crearFase():
    form = fase_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_fase.regFase(nombre = form.nombre.data,
                              posicion = form.posicion.data,
                              descripcion = form.descripcion.data,
                              cantidadItems = form.cantidadItems.data,
                              cantidadLB = form.cantidadLB.data,
                              estado = form.estado.data)
    if resp == 'Exito':
        redirect(url_for('fase'))
    return render_template("fase_crear.html", title = 'Crear fase', form = form)

@app.route('/fase_listar')
@login_required
def fase_listar():
    fase = c_fase.traerFases()  
    return render_template("fase_listar.html", title = 'Listado de fases', Fase = fase)