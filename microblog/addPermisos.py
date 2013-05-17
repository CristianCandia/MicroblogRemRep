'''
Created on 17/05/2013

@author: cristian
'''
#!usr/lib/python

from app import db
from app.modelo import Permiso, Rol
from app.controlador import ControllerRol


p1 = Permiso(nombre='Crear usuario', codigo = '1')
db.session.add(p1)

p2 = Permiso(nombre='Modificar usuario', codigo = '2')
db.session.add(p2)

p3 = Permiso(nombre='Eliminar Usuario', codigo = '3')
db.session.add(p3)

p4 = Permiso(nombre='Crear rol', codigo = '4')
db.session.add(p4)

p5 = Permiso(nombre='Modificar rol', codigo = '5')
db.session.add(p5)

p6 = Permiso(nombre='Eliminar rol', codigo = '6')
db.session.add(p6)

p7 = Permiso(nombre='Asignar rol', codigo = '7')
db.session.add(p7)

p8 = Permiso(nombre='Crear proyecto', codigo = '8')
db.session.add(p8)

p9 = Permiso(nombre='Configurar proyecto', codigo = '9')
db.session.add(p9)

p10 = Permiso(nombre='Modificar proyecto', codigo = '10')
db.session.add(p10)

p11 = Permiso(nombre='Eliminar proyecto', codigo = '11')
db.session.add(p11)

p12 = Permiso(nombre='Ver fase', codigo = '12')
db.session.add(p12)

p13 = Permiso(nombre='Crear Item', codigo = '13')
db.session.add(p13)

p14 = Permiso(nombre='Eliminar item', codigo = '14')
db.session.add(p14)

p15 = Permiso(nombre='Modificar Item', codigo = '15')
db.session.add(p15)

p16 = Permiso(nombre='Crear tipo de item', codigo = '16')
db.session.add(p16)

p17 = Permiso(nombre='Modificar tipo de item', codigo = '17')
db.session.add(p17)

p18 = Permiso(nombre='Eliminar tipo de item', codigo = '18')
db.session.add(p18)

p19 = Permiso(nombre='Crear linea base', codigo = '19')
db.session.add(p19)

p20 = Permiso(nombre='Liberar-cerrar linea base', codigo = '20')
db.session.add(p20)

p21 = Permiso(nombre='Eliminar Linea base', codigo = '21')
db.session.add(p21)

p22 = Permiso(nombre='Aprobar-rechazar item', codigo = '22')
db.session.add(p22)

p23 = Permiso(nombre='Solicitar reportes', codigo = '23')
db.session.add(p23)

p24 = Permiso(nombre='Aprobar-rechazar solicitud de cambio', codigo = '24')
db.session.add(p24)

db.session.commit()


rol2 = Rol(nombre = 'Administrador Principal', descripcion = 'Este rol posee todos los permisos', id_proyecto = 1, id_fase = 1)
db.session.add(rol2)
db.session.commit()

c_rol = ControllerRol()

permisos2 = Permiso.query.all()

for permiso in permisos2:
    c_rol.asignarPermisos(rol2.id, permiso.id)
    
    

