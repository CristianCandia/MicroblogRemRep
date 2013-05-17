"""
Sygma_System
:organization:CRF_Proyect
:author:Cristian Candia
:author:Ruth Centurion
:author:Fernando Saucedo

deleteRol.py
"""

#!usr/lib/python
from app import db
from app.modelo import Rol

roles = Rol.query.all()
for r in roles:
    print "Se elimino " + r.nombre
    db.session.delete(r)
db.session.commit()