"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

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
    def getPermisos(self):
        return Permiso.query.all()
    
    def getPermiso(self, id_permiso):
        return Permiso.query.get(id_permiso)   