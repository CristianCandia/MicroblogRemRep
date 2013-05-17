'''
Created on 20/04/2013

@author: cristian
'''
#!usr/lib/python

#u = models.User.query.get(2)

from app import db, models
from app.modelo import User2


u = User2(name="admin", passWord="admin", nombre="cristian",
                           apellido="candia", telefono="123-321",
                           ci = "4673", e_mail= "@email.com")
db.session.add(u)
db.session.commit()

users = models.User2.query.all()
print users