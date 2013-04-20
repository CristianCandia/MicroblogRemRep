'''
Created on 20/04/2013

@author: cristian
'''
#!usr/lib/python

from app import db, models

u = models.User(name='admin', passWord='admin', role=models.ROLE_ADMIN)
db.session.add(u)
db.session.commit()

users = models.User.query.all()
print users