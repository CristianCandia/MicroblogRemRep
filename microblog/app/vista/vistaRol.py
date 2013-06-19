'''
Created on 03/05/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g

"""Se importa el metodo rol_CrearForm para manipular el formulario"""
from app.forms import rol_CrearForm, asignar_Permisos, buscar, listarPermisos

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerRol, ControllerUsr, ControllerPermiso
from app.modelo import Rol

c_rol = ControllerRol()
c_usr = ControllerUsr()
c_per = ControllerPermiso()

@app.route('/rol')
@app.route('/rol/<idr>')
@login_required
def rol(idr = None):
    roles = c_rol.traerRoles()
    permisosXrol = None
    rol = None
    '''Este if es para recargar la pagina con todos los roles
    mas los permisos del rol que se ha elegido para asignar 
    o desasignar permisos'''
    if idr != None:
        permisosXrol = c_rol.getPermisos_X_Rol(idr)
        rol=c_rol.getRol(idr)
    return render_template("indexRol.html", title='Administracion de Roles',roles=roles,form3=listarPermisos,
                           form=rol_CrearForm(),form2=buscar(),permisos=permisosXrol,permisos2=c_per.getPermisos(), rol=rol)

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


#@app.route('/rol')
#@app.route('/rol/<idr>')

@app.route('/rol/asignar_permisos2/<idr>',methods = ['GET', 'POST'])
@login_required
def asignarPermisos2(idr=None):
    form = listarPermisos()
    
    print ("Prueba1: ",form.u1.data)
    print ("Prueba2: ",form.u2.data)
    print ("Prueba3: ",form.u3.data)
    print ("Prueba4: ",form.u4.data)
    print ("Prueba5: ",form.u5.data)
    print ("Prueba6: ",form.u6.data)
    print ("Prueba4: ",form.u4.data)
    
    flash("se imprimen los true o false del form")
    return redirect(url_for('rol'))

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
    return render_template("indexRol.html", title='Administracion de Roles',roles=roles,form=rol_CrearForm(),form2=buscar(),permisos=None)

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