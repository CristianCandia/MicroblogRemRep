'''
Created on 25/04/2013

@author: cristian
'''

from flask import render_template, flash, redirect, session, url_for, request, g
from app.forms import proy_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerProy
from app.modelo import Proyecto

c_proy = ControllerProy()

@app.route('/proyecto2')
@login_required
def proy2():
    ''' Devuelve los datos de un Usuario en Concreto '''
    proyecto = c_proy.traerProyectos()
    return render_template('indexProy.html', proyectos = proyecto, form = proy_CrearForm())

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
        flash('Proyecto agregado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('proy2'))

@app.route('/proy_listar')
@login_required
def proy_listar():
    proy = c_proy.traerProyectos()  
    return render_template("proy_listar.html", title = 'Listado proyecto', Proyecto = proy)

'''Vista para modificar el usuario'''
@app.route('/proyecto/modificar/', methods = ['GET', 'POST'])
def modificarProyecto():
    form2 = proy_CrearForm()
    resp = None
    if (form2.validate_on_submit()):
        proy = Proyecto()
        proy.nombre = form2.nomProy.data
        proy.decripcion = form2.descripcion.data
        proy.fecha_de_creacion = form2.fecha_de_creacion.data
        proy.complejidad_total = form2.complejidad.data
        proy.estado = form2.estado.data
        
        resp = c_proy.modProyecto(proy)
        
    if(resp == 'Exito'):
        flash('Usuario modificado con exito.')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('usuario'))

@app.route('/proyecto/eliminar/')
@app.route('/proyecto/eliminar/<id>')
def eliminarProy(id=None):
    if(id):
        proyecto = c_proy.getProy(id)
        
        if(proyecto):
            resp = c_proy.eliminarProyecto(proyecto)
            
            if(resp == 'Exito'):
                flash('Proyecto eliminado.')
            else:
                flash('Ocurrio un error: '+str(resp))
        else:
            flash('Ocurrio un error durante la eliminacion.')
    
    return redirect(url_for('proy2'))
