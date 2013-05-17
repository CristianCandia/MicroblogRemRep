'''
Created on 26/04/2013

@author: cristian
'''

from flask import render_template, flash, redirect, session, url_for, request, g
from app.forms import LoginForm, usr_CrearForm, asignar_Roles, rec_passForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, email
from app.controlador import ControllerUsr
from app.modelo import User2
from contextlib import closing
from config import ADMINS



c_usr = ControllerUsr()

'''Vista para agregar un usuario'''
@app.route('/usuario/crear_usr2', methods = ['GET', 'POST'])
@login_required
def crearUsuario():
    form = usr_CrearForm()
    resp = None
    if form.validate_on_submit():
        resp = c_usr.regUsuario(name = form.nomUsr.data, passWord = form.passWord.data, 
                                nombre = form.nombre.data, apellido = form.apellido.data,
                                telefono = form.telefono.data, ci = form.ci.data,
                                e_mail = form.e_mail.data)
    if resp == 'Exito':
        flash('Usuario agregado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    
    return redirect(url_for('usuario'))

'''Vista para modificar el usuario'''
@app.route('/usuario/modificar/', methods = ['GET', 'POST'])
def modificarUsuario():
    form2 = usr_CrearForm()
    resp = None
    print 'antes'
    if (form2.validate_on_submit()):
        print 'despues'
        user = User2()
        user.name = form2.nomUsr.data
        user.passWord = form2.passWord.data
        user.nombre = form2.nombre.data
        user.apellido = form2.apellido.data
        user.telefono = form2.telefono.data
        user.ci = form2.ci.data
        user.e_mail = form2.e_mail.data
        resp = c_usr.modUsuario(user)
        
    if(resp == 'Exito'):
        flash('Usuario modificado con exito.')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('usuario'))

@app.route('/usuario/eliminar/')
@app.route('/usuario/eliminar/<id>')
def eliminarUsuario(id=None):
    if(id):
        usuario = c_usr.getUsr(id)
        
        if(usuario):
            resp = c_usr.eliminarUsr(usuario)
            
            if(resp == 'Exito'):
                flash('Usuario eliminado.')
            else:
                flash('Ocurrio un error: '+str(resp))
        else:
            flash('Ocurrio un error durante la eliminacion.')
    
    return redirect(url_for('usuario'))

@app.route('/rec_pass', methods = ['GET', 'POST'])
def recuperarPass():
    form = rec_passForm()
    if(form.validate_on_submit()):
        user = User2.query.filter_by(name = form.nomUsr.data).first()
        if user is not None:
            email.send_email('Recuperar Pass',
                             ADMINS[0],
                             [user.e_mail],
                             render_template('body_recuperar.txt', user = user),
                             render_template('html_recuperar.html', user = user))
            flash('Le hemos enviado un correo a su cuenta, reviselo!!!')
            return redirect(url_for('login'))
        else:
            flash('El usuario '+str(form.nomUsr.data)+'no existe en el sistema')
    
    return render_template('rec_pass.html',title = 'Recuperar Pass', form = form)
@app.route('/usuario/usuario_asignar_roles' , methods=['GET', 'POST'])

@login_required
def asignarRoles():
    form = asignar_Roles()
    resp = None
    if form.validate_on_submit():
        resp = c_usr.asignarRoles(form.id_usr.data, form.id_rol.data)
    if resp == 'Exito':
        flash('Se ha hecho la asignacion')
        redirect(url_for('usuario'))
    if resp != None:
        flash(resp)
    return render_template("usr_asignar_roles.html",title = 'Asignar Roles', form = form)