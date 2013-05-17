'''
Created on 17/05/2013

@author: cristian
'''
'''
Created on 17/05/2013

@author: cristian
'''
#!usr/lib/python

from app import db
from app.modelo import Permiso, Rol, User2

roles = Rol.query.all()
if roles is not None:
    for rol in roles:
        db.session.delete(rol)
        print "Se elimino" + rol.nombre
    db.session.commit()


permisos = Permiso.query.all()
if permisos is not None:
    for p in permisos:
        db.session.delete(p)
        print "Se elimino" + p.nombre
    db.session.commit()
