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
from app.modelo import Fase

c_fase = ControllerFase()
c_proy = ControllerProy()

@app.route('/fase/')
@app.route('/fase/<idp>')
@login_required
def fase(idp = None):
    fases = c_proy.getFases(idp)
    Proy = c_proy.getProy(idp)
    return render_template("indexFase.html", title = 'Administracion de Fases', fases = fases, Proy = Proy, form = fase_CrearForm())

@app.route('/fase/fase_crear', methods = ['GET', 'POST'])
@app.route('/fase/fase_crear/<idp>', methods = ['GET', 'POST'])
@login_required
def crearFase(idp = None):
    form = fase_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_fase.regFase(nombre = form.nomFase.data,
                              posicion = form.posicion.data,
                              descripcion = form.descripcion.data,
                              cantidadItems = form.cantidadItems.data,
                              cantidadLB = form.cantidadLB.data,
                              estado = form.estado.data,
                              idProy = idp)
    if resp == 'Exito':
        flash('Fase agregada agregada correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('fase',idp=idp))

@app.route('/fase_listar')
@login_required
def fase_listar():
    fase = c_fase.traerFases()  
    return render_template("fase_listar.html", title = 'Listado de fases', Fase = fase)

'''Vista para modificar fase'''
@app.route('/fase/modificar/', methods = ['GET', 'POST'])
def modificarFase():
    form2 = fase_CrearForm()
    resp = None
    if (form2.validate_on_submit()):
        fase = Fase()
        fase.id = form2.idFase.data
        fase.nombre = form2.nomFase.data
        fase.posicion = form2.posicion.data
        fase.descripcion = form2.descripcion.data
        fase.cantidadItems = form2.cantidadItems.data
        fase.cantidadLB = form2.cantidadLB.data
        fase.estado = form2.estado.data
        resp = c_fase.modFase(fase)
        
    if(resp == 'Exito'):
        flash('Fase modificada con exito.')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('fase',idp = form2.idProy.data))

@app.route('/fase/eliminar/')
@app.route('/fase/eliminar/<idf>,<idp>')
def eliminarFase(idf = None, idp = None):
    if(idf):
        fase = c_fase.getFase(idf)
        if(fase):
            resp = c_fase.eliminarFase(fase)
            if(resp == 'Exito'):
                flash('Fase eliminada.')
            else:
                flash('Ocurrio un error: '+str(resp))
        else:
            flash('Ocurrio un error durante la eliminacion.')
    
    return redirect(url_for('fase', idp=idp))
