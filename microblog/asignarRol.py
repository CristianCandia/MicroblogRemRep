'''
Created on 17/05/2013

@author: cristian
'''
from app import db
from app.modelo import Rol, User2
from app.controlador import ControllerUsr

user = User2.query.filter_by(name = 'admin').first()

print user.id

rol = Rol.query.filter_by(nombre = 'Administrador Principal').first()

print rol.nombre

c_usr = ControllerUsr()

c_usr.asignarRoles(user.id, rol.id)

print "Acaba de asignar el rol de administrador principal a admin"

