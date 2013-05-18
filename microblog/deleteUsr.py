"""
Sygma_System
:organization:CRF_Proyect
:author:Cristian Candia
:author:Ruth Centurion
:author:Fernando Saucedo

deleteUsr.py
"""

#!usr/lib/python
from app import db, models
from app.modelo import User2
users = User2.query.all()
for u in users:
    db.session.delete(u)
    print "Se elimino " + u.name
db.session.commit()