'''
Created on 17/05/2013

@author: cristian
'''
#!usr/lib/python

from app import db
from app.modelo import Permiso, Rol
from app.controlador import ControllerRol


try:   
    p1 = Permiso(id = 1, nombre='Crear usuario', codigo = '1')
    db.session.add(p1)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))
   
try:
    p2 = Permiso(id = 2, nombre='Modificar usuario', codigo = '2')
    db.session.add(p2)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p3 = Permiso(id = 3, nombre='Eliminar Usuario', codigo = '3')
    db.session.add(p3)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))
   
try:
    p4 = Permiso(id = 4, nombre='Crear rol', codigo = '4')
    db.session.add(p4)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))
   
try:
    p5 = Permiso(id = 5, nombre='Modificar rol', codigo = '5')
    db.session.add(p5)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))
   
try:
    p6 = Permiso(id = 6, nombre='Eliminar rol', codigo = '6')
    db.session.add(p6)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))
   
try:
    p7 = Permiso(id = 7, nombre='Asignar rol', codigo = '7')
    db.session.add(p7)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))
   
try:
    p8 = Permiso(id = 8, nombre='Crear proyecto', codigo = '8')
    db.session.add(p8)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p9 = Permiso(id = 9, nombre='Configurar proyecto', codigo = '9')
    db.session.add(p9)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p10 = Permiso(id = 10, nombre='Modificar proyecto', codigo = '10')
    db.session.add(p10)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:   
    p11 = Permiso(id = 11, nombre='Eliminar proyecto', codigo = '11')
    db.session.add(p11)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try: 
    p12 = Permiso(id = 12, nombre='Ver fase', codigo = '12')
    db.session.add(p12)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:   
    p13 = Permiso(id = 13, nombre='Crear Item', codigo = '13')
    db.session.add(p13)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:   
    p14 = Permiso(id = 14, nombre='Eliminar item', codigo = '14')
    db.session.add(p14)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p15 = Permiso(id = 15, nombre='Modificar Item', codigo = '15')
    db.session.add(p15)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:   
    p16 = Permiso(id = 16, nombre='Crear tipo de item', codigo = '16')
    db.session.add(p16)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p17 = Permiso(id = 17, nombre='Modificar tipo de item', codigo = '17')
    db.session.add(p17)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:   
    p18 = Permiso(id = 18, nombre='Eliminar tipo de item', codigo = '18')
    db.session.add(p18)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p19 = Permiso(id = 19, nombre='Crear linea base', codigo = '19')
    db.session.add(p19)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p20 = Permiso(id = 20, nombre='Liberar-cerrar linea base', codigo = '20')
    db.session.add(p20)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p21 = Permiso(id = 21, nombre='Eliminar linea base', codigo = '21')
    db.session.add(p21)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p22 = Permiso(id = 22, nombre='Aprobar-rechazar item', codigo = '22')
    db.session.add(p22)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p23 = Permiso(id = 23, nombre='Solicitar reportes', codigo = '23')
    db.session.add(p23)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))

try:
    p24 = Permiso(id = 24, nombre='Aprobar-rechazar solicitud de cambio', codigo = '24')
    db.session.add(p24)
    db.session.commit()
    print 'Permiso %s registrado' % (nombre)
except Exception, error:
    db.session.rollback()
    print 'No se pudo cargar el permiso %s: %s' % (nombre, str(error))


c_rol = ControllerRol()
rol2 = Rol.query.filter_by(nombre = 'Administrador Principal').first()

permisos2 = Permiso.query.all()

for permiso in permisos2:
    c_rol.asignarPermisos(rol2.id, permiso.id)