'''
Created on 20/04/2013

@author: cristian
'''
#!usr/lib/python

#u = models.User.query.get(2)

from app import db, models
from app.modelo import User2, Rol, Proyecto, Fase

u = User2(name="admin", passWord="admin", nombre="cristian",
                           apellido="candia", telefono="123-321",
                           ci = "4673", e_mail= "@email.com")
db.session.add(u)
db.session.commit()

p = Proyecto(id = 1, nombre = 'Proyecto inicial', descripcion = 'Proyecto inicial de prueba', estado='Abierto')
db.session.add(p)
db.session.commit

f = Fase(id=1, nombre = 'Fase 1', posicion = 1, descripcion = 'fase 1 inicial', cantidadItems = 5, cantidadLB = 5, estado = 'Abierto', id_proyecto = 1)
db.session.add(f)
db.session.commit

r = Rol(nombre ='Administrador Principal',descripcion = 'Posee todos los permisos', id_proyecto = 1, id_fase = 1)
db.session.add(r)
db.session.commit()

users = User2.query.all()
print users