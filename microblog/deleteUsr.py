'''
Created on 20/04/2013

@author: cristian
'''

#!usr/lib/python
from app import db, models

users = models.User.query.all()
for u in users:
    db.session.delete(u)
    
db.session.commit()