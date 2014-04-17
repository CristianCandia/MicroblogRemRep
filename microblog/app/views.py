"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, usr_CrearForm, buscar
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm #models, oid
from models import ROLE_USER, ROLE_ADMIN
from app.modelo import User2
from app.controlador import ControllerUsr

user1=None

@lm.user_loader
def load_user(id):
    return User2.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user#{ 'nickname': 'Miguel' } # fake user
    ''' posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautifukjhvgjl day hvjhvin Portland!'
        },
        { 
            'author': { 'nickname'jvjhgvhj: 'Susan' },
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_temphkjgbjklate("index.html",
        title = 'Home',
        user = user)'''
    return redirect('admin')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User2.query.filter_by(name = form.nomUsr.data).first()
        if user is not None:
            if user.passWord == form.passWord.data:
                session['logged_in'] = True
                session['permisos'] = c_user.getPermisos(user)
                flash('Has iniciado sesion')
                login_user(user)
                global user1
                user1 = user
                return redirect(url_for('admin'))
            else:
                flash('Pass incorrecto, ingresela de nuevo')
        else:
            flash('Usuario no existente, pongase en contacto con el administrador para obtener una cuenta')
            return render_template('login.html',title = 'Iniciar Sesion',form = form)
    return render_template('login.html',title = 'Iniciar Sesion',form = form)         
    
@app.before_request
def before_request():
    g.user = current_user    
    

@app.route('/admin')
@login_required
def admin():
    return render_template("admin.html", title = 'Administrador General', session = session['permisos'], usuario = user1)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#todo lo que hizo fernando saucedo
c_user = ControllerUsr()

def listadoUsuarios():
    ''' Devuelve un listado de los usuarios '''
    lista = None
    r = True
    if(r):
        lista = c_user.getUsrFull()
    else:
        flash("Error. Lista no devuelta")
    return lista

@app.route('/usuario')
@login_required
def usuario():
    ''' Devuelve los datos de un Usuario en Concreto '''
    usuarios = listadoUsuarios();
    return render_template('indexUser.html', usuarios = usuarios, form = usr_CrearForm(), form2 = buscar())

#hasta aca

@app.route('/usr_crear', methods = ['GET', 'POST'])
@login_required
def usr_crear():
    form = usr_CrearForm()
    if form.validate_on_submit():
            if form.nomUsr.data != '':
                if form.passWord.data != '':
                    if buscar_str(form.nomUsr.data) != True:
                        u = User2(name=form.nomUsr.data, passWord=form.passWord.data, role=ROLE_ADMIN)
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
    users = User2.query.all()
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
    users = User2.query.all()
    return render_template("usr_listar.html", title = 'Listado usuario',User = users)
                
    