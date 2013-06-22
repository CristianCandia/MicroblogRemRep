"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from app.controlador import ControllerFase, ControllerProy, ControllerTI, ControllerAtributoTI
from app.modelo import Item, TipoItem, AtributoPorTI
from app.forms import crear_mod_atributoTI

c_fase = ControllerFase()
c_proy = ControllerProy()
c_TI = ControllerTI()
c_atribTI = ControllerAtributoTI()

@app.route('/TI/atributo/')
@app.route('/TI/atributo/<idTI>,<idp>,<idf>')
@login_required
def atributoTI(idTI = None, idp = None, idf = None):
    """
        Vista que da acceso a la pagina de los atributos del TI
        que es pasado como parametro
    """
    fase = c_fase.getFase(idf)
    proy = c_proy.getProy(idp)
    TI = c_TI.getTIId(idTI)
    b = 0
    for f in TI:
        if b == 0:
            w = f
            b = 1
    form = crear_mod_atributoTI()
    atributos = c_atribTI.getAtributoTIId(idTI)
    return render_template("indexAtributoTI.html",
                           title='Atributos de Tipos de Items',
                           fase = fase,
                           proyecto = proy,
                           TI = w,
                           form = form,
                           atributos = atributos)

@app.route('/TI/atributo/crear/', methods=['GET','POST'])
@app.route('/TI/atributo/crear/<idTI>,<idp>,<idf>', methods=['GET','POST'])
@login_required
def crearAtributoTI(idTI = None, idp = None, idf = None):
    """
        Vista para crear el Tipo de Item
        @param idf: id de la fase asociada.
        @param idp: id del proyecto asociado.
    """
    form = crear_mod_atributoTI()
    resp = None
    if form.validate_on_submit():
        atribTI = AtributoPorTI(idTI, form.nombre.data, form.tipo.data, form.valorDefault.data)
        resp = c_atribTI.regAtributoTI(atribTI)
    else:
        resp = 'Complete todos los datos obligatorios'
    if resp == 'Exito':
        
        flash('Tipo de Item agregado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('atributoTI',idTI=idTI, idp=idp, idf=idf))

@app.route('/TI/atributo/modificar/', methods = ['GET', 'POST'])
@app.route('/TI/atributo/modificar/<idATI><idTI>,<idf>,<idp>', methods = ['GET', 'POST'])
@login_required
def modificarAtributoTI(idATI = None, idTI = None, idf = None, idp = None):
    """
        Vista que modifica un Atributo de un TipoItem.
    """
    resp = None
    form = crear_mod_atributoTI()
    resp = None
    if form.validate_on_submit():
        TI = AtributoPorTIAtributoPorTI(idTI, form.nombre.data, form.tipo.data, form.valorDefault.data)
        
        TI.id_Atrib_TI = idATI
        resp = c_atribTI.modAtributoTI(TI)
    else:
        resp = 'Complete todos los datos obligatorios'
    if resp == 'Exito':
        flash('Atributo de Tipo de Item modificado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('atributoTI',idTI=idTI, idp=idp, idf=idf))

@app.route('/TI/atributo/eliminar/', methods = ['GET', 'POST'])
@app.route('/TI/atributo/eliminar/<idATI>,<idTI>,<idf>,<idp>', methods = ['GET', 'POST'])
@login_required
def eliminarTI(idATI = None, idTI = None, idf = None, idp = None):
    """
        Vista correspondiente a la eliminacion de un Atributo de un Tipo de Item
    """
    resp = None
    TI = c_TI.getTIId(idTI)
    if (TI == []):
        print 'Vacio'
        flash('Ocurrio un error: ' + str(resp))
        return redirect(url_for('TI',idp=idp, idf=idf))
    else:
        for f in TI:
            if (f.items != []):
                flash('No puedes eliminarlo, este TI esta instanciado')
                return redirect(url_for('atributoTI',idTI=idTI, idp=idp, idf=idf))
            atrib = c_atribTI.getAtributoTIIdA(idATI)
            if(atrib):
                resp = delAtributoTI(atrib)
                if resp == 'Exito':
                    flash('Tipo de Item eliminado correctamente')
                else:
                    flash('Ocurrio un error: ' + str(resp))
                return redirect(url_for('atributoTI',idTI=idTI, idp=idp, idf=idf))