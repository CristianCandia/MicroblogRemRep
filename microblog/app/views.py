'''
Created on 14/04/2013

@author: cristian
'''
from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, usr_CrearForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user#{ 'nickname': 'Miguel' } # fake user
    ''' posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]'''
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name = form.nomUsr.data).first()
        if user is not None:
            if user.passWord == form.passWord.data:
                session['logged_in'] = True
                flash('Has iniciado sesion')
                login_user(user)
                return redirect(url_for('admin'))
        flash('Fallo en el logueo. Por favor, intente de nuevo.')       
    return render_template('login.html',title = 'Iniciar Sesion',form = form)           
      
@app.before_request
def before_request():
    g.user = current_user    
    

@app.route('/admin')
@login_required
def admin():
    return render_template("admin.html", title = 'Administrador General')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/usuario')
@login_required
def usuario():
    return render_template("usuario.html", title = 'Administracion de usuario')




@app.route('/usr_crear', methods = ['GET', 'POST'])
@login_required
def usr_crear():
    form = usr_CrearForm()
    if form.validate_on_submit():
            if form.nomUsr.data != '':
                if form.passWord.data != '':
                    if buscar_str(form.nomUsr.data) != True:
                        u = User(name=form.nomUsr.data, passWord=form.passWord.data, role=ROLE_ADMIN)
                        db.session.add(u)
                        db.session.commit()
                        flash('Se ha creado un nuevo usuario')
                    else:
                        return redirect('/usuario')
                else:
                    return redirect('/usuario')    
    flash('Ingrese correctamente los datos')                    
    return render_template("usr_crear.html", title = 'Crear usuario', form = form)

@app.route('/usr_modificar')
@login_required
def usr_modificar():
    return render_template("usr_modificar.html", title = 'Modificar usuario')

@app.route('/usr_eliminar')
@login_required
def usr_eliminar():
    return render_template("usr_eliminar.html", title = 'Eliminar usuario')

def buscar_str(nom):
    users = User.query.all()
    ban = 0
    for u in users:
        if u.name == nom:
            ban = 1
    if ban == 1:
        return True
    return False
                
@app.route('/usr_listar')
@login_required
def usr_listar():
    users = User.query.all()
    return render_template("usr_listar.html", title = 'Listado usuario',User = users)
                
    