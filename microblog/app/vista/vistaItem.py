"""
@note: Clase que define la vista de Item
@authors:
    - U{Cristian Candia<mailto:kandia88@gmail.com>}
    - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
    - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_required
from app import app
from app.controlador import ControllerItem, ControllerProy, ControllerFase

c_item = ControllerItem()
c_proyecto = ControllerProy()
c_fases = ControllerFase()

@app.route('/item_fase/<id>/nuevo', methods = ['GET', 'POST'])
@login_required
def nuevoItem(id=None):
    pass

@login_required
def listadoItemFase(id):
    '''Devuelve un listado de todos los items de la fase pasada como parametro'''
    lista = None
    r = True
    lista2 = None
    count = 0
    if (r):
        lista = c_item.getItemAll()
    else:
        flash('Se produjo un error, no podemos devolverle una lista')
    return lista

@app.route('/item/fase/', methods = ['GET', 'POST'])
@app.route('/item/fase/<id>', methods = ['GET', 'POST'])
@login_required
def itemFase(id = None):
    items = listadoItemFase(request.form['id_fase'])
    print str(items)
    fase = c_fases.getFase(request.form['id_fase'])
    proyecto = c_proyecto.getProy(fase.id_proyecto) 
    return render_template('indexItem.html', item = items, fase = fase, proyecto = proyecto)
    

@login_required
def listadoFases():
    '''Devuelve un listado de todos los items de la fase pasada como parametro'''
    lista = None
    r = True
    if (r):
        lista = c_fases.traerFases()
    else:
        flash('Se produjo un error, no podemos devolverle una lista')
    return lista

@login_required
def listadoProyectos():
    '''Devuelve un listado de todos los items de la fase pasada como parametro'''
    lista = None
    r = True
    if (r):
        lista = c_proyecto.traerProyectos()
    else:
        flash('Se produjo un error, no podemos devolverle una lista')
    return lista

@app.route('/item/proy/')
@login_required
def itemProy():
    proyectos = listadoProyectos()
    fases = listadoFases()
    print str(proyectos)
    return render_template('MPI.html', proyecto = proyectos, fase = fases)

@app.route('/item/nuevo', methods = ['GET', 'POST'])
@login_required
def nuevoItem():
    pass