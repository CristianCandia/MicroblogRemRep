'''
Created on 14/04/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session
from forms import LoginForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, models#, oid
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)



@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = models.User.query.all()
        ban = 0
        for u in users:
            if u.name == form.nomUsr.data:
                ban = 1
                if u.passWord == form.passWord.data:
                    session['logged_in'] = True
                    flash('Has iniciado sesion')
                    return redirect('/admin')
                else:
                    err = 'Ingrese correctamente su contraseña'
        if ban == 0:
            err = 'No existe nombre de usuario'
            return render_template('login.html',title = 'Iniciar Sesion',form = form, err=err)
    else:
        err = 'Complete correctamente los campos'                    
        return render_template('login.html',title = 'Iniciar Sesion',form = form, err=err)
    
@app.route('/admin')
def admin():
    return render_template("admin.html", title = 'Administrador General')

@app.route('/usuario')
def usuario():
    return render_template("usuario.html", title = 'Administracion de usuario')

@app.route('/usr_crear')
def usr_crear():
    return render_template("usr_crear.html", title = 'Crear usuario')

@app.route('/usr_modificar')
def usr_modificar():
    return render_template("usr_modificar.html", title = 'Modificar usuario')

@app.route('/usr_eliminar')
def usr_eliminar():
    return render_template("usr_eliminar.html", title = 'Eliminar usuario')

