'''
Created on 03/05/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g

"""Se importa el metodo rol_CrearForm para manipular el formulario"""
from app.forms import rol_CrearForm, asignar_Permisos, buscar

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerRol, ControllerUsr
from app.modelo import Rol

c_rol = ControllerRol()
c_usr = ControllerUsr()

@app.route('/rol')
@login_required
def rol():
    roles = c_rol.traerRoles()
    return render_template("indexRol.html", title='Administracion de Roles',roles=roles,form=rol_CrearForm(),form2=buscar())

@app.route('/rol/rol_crear', methods = ['GET', 'POST'])
@login_required
def crearRol():
    form = rol_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_rol.regRol(nombre = form.nomRol.data,
                            descripcion = form.descripcion.data)
    if resp == 'Exito':
        flash('Rol agregado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('rol'))

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

'''Vista para modificar rol'''
@app.route('/rol/modificar/', methods = ['GET', 'POST'])
def modificarRol():
    form2 = rol_CrearForm()
    resp = None
    if (form2.validate_on_submit()):
        rol = Rol()
        rol.id = form2.idRol.data
        rol.nombre = form2.nomRol.data
        rol.descripcion = form2.descripcion.data
        resp = c_rol.modRol(rol)
        
    if(resp == 'Exito'):
        flash('Rol modificado con exito.')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('rol'))

@app.route('/rol/buscar', methods = ['GET', 'POST'])
def buscarRol(idu = None):
    ''' Devuelve una lista de roles que coincidan con el nombre proporcionado '''
    form2 = buscar()
    roles = c_rol.buscarPorNombreRol(form2.nombreBuscado.data)
    return render_template("indexRol.html", title='Administracion de Roles',roles=roles,form=rol_CrearForm(),form2=buscar())

@app.route('/rol/eliminar/')
@app.route('/rol/eliminar/<idr>')
def eliminarRol(idr = None):
    if(idr):
        rol = c_rol.getRol(idr)
        if(rol):
            resp = c_rol.eliminarRol(rol)
            if(resp == 'Exito'):
                flash('Rol eliminado.')
            else:
                flash('Ocurrio un error: '+str(resp))
        else:
            flash('Ocurrio un error durante la eliminacion.')
    
    return redirect(url_for('rol'))
