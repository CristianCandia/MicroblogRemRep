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


@app.route('/rol/proyFase/<id1>/<id2>/<opcion>')
@login_required
def rol_proyFase(id1=None, id2=None, opcion=None):
    if id1 != None:
        roles = c_rol.getRolIdf(id1)
    permisosXrol = None
    rol = None
    '''Este if es para recargar la pagina con todos los roles
    mas los permisos del rol que se ha elegido para asignar 
    o desasignar permisos'''
    if id2 != None and int(opcion) == 2:
        print "entro en opcion 2"
        permisosXrol = c_rol.getPermisos_X_Rol(id2)
        rol=c_rol.getRol(id2)
    return render_template("indexRol2.html", title='Administracion de Roles',roles=roles,form3=listarPermisos,
                           form=rol_CrearForm(),form2=buscar(),permisos=permisosXrol,permisos2=c_per.getPermisos(), 
                           rol=rol, idf=id1)

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

@app.route('/rol/rol_crear/<idf>', methods = ['GET', 'POST'])
@login_required
def crearRol(idf = None):
    form = rol_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_rol.regRol(nombre = form.nomRol.data,
                            descripcion = form.descripcion.data, idf = idf)
    if resp == 'Exito':
        flash('Rol agregado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('rol_proyFase', id1=idf, id2=idf, opcion = 1))

@app.route('/rol_listar')
@login_required
def rol_listar():
    rol = c_rol.traerRoles()  
    return render_template("rol_listar.html", title = 'Listado de roles', Rol = rol)


@app.route('/rol/asignarRoles/<idr>/<idf>', methods = ['post', 'get'])
@login_required 
def asignarRoles(idr = None, idf = None):
    usr = c_rol.usrSinRolIdr(idr)
    return render_template("usr_asignar_roles.html",usr=usr,idr=idr)

@app.route('/rol/asigUsrRol/<idr>', methods = ['GET', 'POST'])
@login_required 
def asigUsrRol(idr = None):
    if request.method == 'POST':
        usr = request.form.getlist('listado')
        if usr != None:
            respuesta = c_usr.asignarRolAListaDeUsr(usr, idr)
            print "se puede hacer algo"
        else:
            print "no se puede hacer nada por ahora"
        if respuesta == 'Exito':
            flash("Se ha asignado correctamente") 
                  
    return redirect(url_for('rol_proyFase',id1=c_rol.getIdfaseDeRol(idr),id2=0,opcion=1))

@app.route('/rol/asignar_permisos2/<idr>/<idf>', methods = ['post', 'get'])
@login_required 
def asignarPermisos2(idr=None, idf=None):
    form = listarPermisos() 
    lista = []
    if form.validate_on_submit():
        ban = 0
        for f in form:
            if ban == 1:
                datos = f.id.split('u')
                l = {'id':int(datos[1]), 'dato':f.data}
                #print l['id'], l['dato']
                lista.append(l)
            ban = 1
    respuesta = c_rol.asignarDesasginarPer(idr, lista)
    ban = 0
    for r in respuesta:
        if r['error'] == 1:
            ban = 1
            break
        if r['error'] == 2:
            ban = 2
            break
    if ban == 0:    
        flash("Se realizaron correctamente las asignaciones/desasignaciones")
    else:
        if ban == 1:
            flash("Error en algunas de las las asignaciones")
        if ban == 2:
            flash("Error en algunas de las las desasignaciones")
                
    return redirect(url_for('rol_proyFase',id1=idf,id2=idf,opcion=1))

'''Vista para modificar rol'''
@app.route('/rol/modificar/<idf>', methods = ['GET', 'POST'])
def modificarRol(idf = None):
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
    return redirect(url_for('rol_proyFase',id1=idf,id2=idf,opcion = 1))

@app.route('/rol/buscar', methods = ['GET', 'POST'])
def buscarRol(idu = None):
    ''' Devuelve una lista de roles que coincidan con el nombre proporcionado '''
    form2 = buscar()
    roles = c_rol.buscarPorNombreRol(form2.nombreBuscado.data)
    return render_template("indexRol.html", title='Administracion de Roles',roles=roles,form=rol_CrearForm(),form2=buscar(),permisos=None)

@app.route('/rol/eliminar/')
@app.route('/rol/eliminar/<idr>/<idf>')
def eliminarRol(idr=None, idf=None):
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
    return redirect(url_for('rol_proyFase',id1=idf,id2=idf,opcion = 1))