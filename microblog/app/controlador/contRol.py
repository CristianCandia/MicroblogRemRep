'''
Created on 02/05/2013

@author: cristian
'''
from app.modelo import Rol
class ControllerRol():
    def regRol(self, **kwargsProy):
        rol = Rol()
        for k, v in kwargsProy.iteritems():
            if k == 'nombre':
                rol.nombre = v
            if k == 'descripcion':
                rol.descripcion = v
        return rol.add_rol()
    def traerRoles(self):
        return Rol.query.all()