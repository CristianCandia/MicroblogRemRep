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
from app.controlador import ControllerFase, ControllerProy, ControllerTI
from app.modelo import Item, TipoItem
from app.forms import crear_mod_TI

c_proy = ControllerProy()
c_TI = ControllerTI()
c_fase = ControllerFase()

@app.route('/TI/')
@app.route('/TI/<idp>,<idf>')
@login_required
def TI(idp = None, idf = None):
    fase = c_fase.getFase(idf)
    proy = c_proy.getProy(idp)
    TI = c_TI.getTIFase(fase.id)
    form = crear_mod_TI()
    return render_template("indexTI.html",
                           title='Administracion de Tipos de Items',
                           fase = fase,
                           proyecto = proy,
                           TI = TI,
                           form = form)
@app.route('/TI/crear/', methods = ['GET', 'POST'])
@app.route('/TI/crear/<idf>,<idp>', methods = ['GET', 'POST'])
@login_required
def crearTI(idf = None, idp = None):
    """
        Vista para crear el Tipo de Item
        @param idf: id de la fase asociada.
        @param idp: id del proyecto asociado.
    """
    form = crear_mod_TI()
    resp = None
    if form.validate_on_submit():
        TI = TipoItem(form.codigo.data, form.nombre_TI.data, form.descripcion.data,
                      idp, idf)
        resp = c_TI.regTI(TI)
        print str(resp)
        try:
            TI.codigo = "SS" + str(idp) + "_F"+ str(idf) + "_TI" + str(TI.id_TI)
            db.session.merge(TI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            resp = str(error)
    else:
        resp = 'Complete todos los datos obligatorios'
    if resp == 'Exito':
        
        flash('Tipo de Item agregado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('TI',idp=idp, idf=idf))



@app.route('/TI/modificar/', methods = ['GET', 'POST'])
@app.route('/TI/modificar/<idTI>,<idf>,<idp>', methods = ['GET', 'POST'])
@login_required
def modificarTI(idTI = None, idf = None, idp = None):
    """
        Vista que modifica un TipoItem.
    """
    resp = None
    form = crear_mod_TI()
    resp = None
    if form.validate_on_submit():
        TI = TipoItem(form.codigo.data, form.nombre_TI.data, form.descripcion.data,
                      idp, idf)
        TI.id_TI = idTI
        resp = c_TI.modTI(TI)
    else:
        resp = 'Complete todos los datos obligatorios'
    if resp == 'Exito':
        flash('Tipo de Item modificado correctamente')
    else:
        flash('Ocurrio un error: ' + str(resp))
    return redirect(url_for('TI',idp=idp, idf=idf))

@app.route('/TI/eliminar/', methods = ['GET', 'POST'])
@app.route('/TI/eliminar/<idTI>,<idf>,<idp>', methods = ['GET', 'POST'])
@login_required
def eliminarTI(idTI = None, idf = None, idp = None):
    """
        Vista correspondiente a la eliminacion de un Tipo de Item
    """
    print "entro en submit"
    print "entro en submit"
    print "entro en submit"
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
                return redirect(url_for('TI',idp=idp, idf=idf))
            resp = c_TI.delTI(f)
            if resp == 'Exito':
                flash('Tipo de Item eliminado correctamente')
            else:
                flash('Ocurrio un error: ' + str(resp))
            return redirect(url_for('TI',idp=idp, idf=idf))