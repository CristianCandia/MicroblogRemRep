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

users = models.User.query.all()
for u in users:
    db.session.delete(u)
    
db.session.commit()