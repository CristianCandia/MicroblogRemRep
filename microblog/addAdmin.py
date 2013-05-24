'''
Created on 20/04/2013

@author: cristian
'''
#!usr/lib/python

#u = models.User.query.get(2)

from app import db, models
from app.modelo import User2, Rol, Proyecto, Fase
'''
    Agregamos el usuario administrador
'''
try:
    u = User2(name="admin", passWord="admin", nombre="sigma",
                               apellido="system", telefono="123-321",
                               ci = "4673", e_mail= "sigmasystem21@gmail.com")
    db.session.add(u)
    db.session.commit()
    print 'Usuario registrado' 
except Exception, error:
    db.session.rollback()
    print 'Error al guardar usuario: ' + str(error)

'''
    Se agrega el primer proyecto al sistema
'''
try:
    p = Proyecto(id = 1, nombre = 'Proyecto inicial', descripcion = 'Proyecto inicial de prueba', estado='Abierto')
    db.session.add(p)
    db.session.commit()
    print 'Proyecto registrado'
except Exception, error:
    db.session.rollback()
    print 'No se pudo agregar el Proyecto: ' + str(error)

'''
    Se agrega una fase al proyecto
'''
try:
    f = Fase(id=1, nombre = 'Fase 1', posicion = 1, descripcion = 'fase 1 inicial', cantidadItems = 5, cantidadLB = 5, estado = 'Abierto', id_proyecto = 1)
    db.session.add(f)
    db.session.commit()
    print 'Fase registrada'
except Exception, error:
    db.session.rollback()
    print 'No se pudo agregar la fase: ' + str(error)

'''
    Se agrega un rol al sistema
'''

try:
    r = Rol(nombre ='Administrador Principal',descripcion = 'Posee todos los permisos', id_proyecto = 1, id_fase = 1)
    db.session.add(r)
    db.session.commit()
    print 'Rol registrado'
except Exception, error:
    db.session.rollback()
    print 'No se pudo agregar el rol: ' + str(error)

users = User2.query.all()
print users