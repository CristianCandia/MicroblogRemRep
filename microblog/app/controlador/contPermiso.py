'''
Created on 02/05/2013

@author: cristian
'''
from app.modelo import Permiso
class ControllerPermiso():
    def regPermiso(self, **kwargsProy):
        permiso = Permiso()
        for k, v in kwargsProy.iteritems():
            if k == 'nombre':
                permiso.nombre = v
            if k == 'codigo':
                permiso.codigo = v
        return permiso.add_permiso()
    def traerPermisos(self):
        return Permiso.query.all()