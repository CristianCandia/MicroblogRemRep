'''
Created on 25/04/2013

@author: cristian
'''

from flask import render_template, flash, redirect, session, url_for, request, g
from app.forms import proy_CrearForm, buscar, comite_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from app.controlador import ControllerProy, ControllerComite
from app.modelo import Proyecto

c_comite = ControllerComite()
c_proy = ControllerProy()

@app.route('/proyecto2')
@login_required
def proy2():
    ''' Devuelve los datos de un Proyecto en Concreto '''
    proyecto = c_proy.traerProyectos()
    return render_template('indexProy.html', proyectos = proyecto, form = proy_CrearForm(), form2 = buscar())

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
                                  fecha_de_creacion = form.fecha_de_creacion.data,
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

'''Vista para modificar el proyecto'''
@app.route('/proyecto/modificar/', methods = ['GET', 'POST'])
@login_required
def modificarProyecto():
    form2 = proy_CrearForm()
    resp = None
    if (form2.validate_on_submit()):
        proy = Proyecto()
        proy.id = form2.idProy.data
        proy.nombre = form2.nomProy.data
        proy.descripcion = form2.descripcion.data
        proy.fecha_de_creacion = form2.fecha_de_creacion.data
        proy.complejidad_total = form2.complejidad.data
        proy.estado = form2.estado.data
        
        resp = c_proy.modProyecto(proy)
        
    if(resp == 'Exito'):
        flash('Proyecto modificado con exito.')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('proy2'))

@app.route('/proyecto/eliminar/')
@app.route('/proyecto/eliminar/<id>')
@login_required
def eliminarProy(id = None):
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


'''Vista para configurar el proyecto'''
@app.route('/proyecto/configurar/', methods = ['GET', 'POST'])
@app.route('/proyecto/configurar/<idp>')
@login_required
def configurarProyecto(idp = None):
    nomProy = c_proy.getNombre(idp)
    return render_template("proy_configurar.html", title = 'Configurar Proyecto', nomProy = nomProy, idp=idp,resp=c_comite.hayComite(idp))


@app.route('/proyecto/crear_comite/<idp>', methods = ['GET', 'POST'])
@login_required
def crearComite(idp = None):
    resp = None
    if request.method == 'POST':
        print request.form['nomComite']
        print request.form['u1']
        resp = c_comite.regComite(nombre = request.form['nomComite'],
                                  cant_miembros = int(request.form['u1']),
                                  id_proyecto = idp)
    if(resp == 'Exito'):
        flash('Comite inicializado con exito.')
    else:
        flash('Ocurrio un error: ' + str(resp))
    nomProy = c_proy.getNombre(idp)
    return render_template("proy_configurar.html", title = 'Configurar Proyecto', nomProy = nomProy, idp=idp, form = comite_CrearForm())

@app.route('/proyecto/asignarMiembros/<idp>', methods = ['post', 'get'])
@login_required 
def asignarMiembros(idp = None):
    com = c_comite.getComiteXIdp(idp)
    usr = c_comite.usrSinComiteIdc(com.id)
    return render_template("comite_asig_usr.html",usr=usr,idp=idp,idc=com.id)

@app.route('/proyecto/asigUsrComite/<idc>', methods = ['GET', 'POST'])
@login_required 
def asigUsrComite(idc = None):
    proy = c_proy.getProy(c_comite.getComite(idc).id_proyecto)
    if request.method == 'POST':
        usr = request.form.getlist('listado')
        print usr
        if usr != None:
            respuesta = c_comite.asignarComiteAListaDeUsr(usr, idc)
            print "se puede hacer algo"
        else:
            print "no se puede hacer nada por ahora"
        if respuesta == 'Exito':
            flash("Se ha asignado correctamente") 
    return render_template("proy_configurar.html", title = 'Configurar Proyecto', nomProy = proy.nombre, idp=proy.id,resp=1)


@app.route('/proyecto/buscar', methods = ['GET', 'POST'])
@login_required
def buscarProyecto():
    ''' Devuelve una lista de proyectos que coincidan con el nombre proporcionado '''
    form2 = buscar()
    proyectos = c_proy.buscarPorNombreProyecto(form2.nombreBuscado.data)
    return render_template('indexProy.html', proyectos = proyectos, form = proy_CrearForm(), form2=form2)