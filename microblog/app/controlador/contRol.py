'''
Created on 02/05/2013

@author: cristian
'''

from app.modelo import Rol
from app import db 
from app.controlador.contPermiso import ControllerPermiso
 


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
    
    def getRol(self, id):
        return Rol.query.get(id)
    
    def eliminarRol(self, rol):
        return rol.delete_rol()
    
    def asignarPermisos(self,id_rol,id_permiso):
        c_permiso = ControllerPermiso()
        
        rol = self.getRol(id_rol)
        permiso = c_permiso.getPermiso(id_permiso)
        
        if rol != None and permiso != None:
            rol.permisos.append(permiso)
            try:
                db.session.merge(rol)
                db.session.commit()
            except Exception, error:
                db.session.rollback()
                return error
            return 'Exito'
        return 'No existen el/los id(s) ingresados'
    
    def modRol(self, rolAux):
        rol = self.getRol(rolAux.id)
        rol.nombre = rolAux.nombre
        rol.descripcion = rolAux.descripcion
        try:
            db.session.merge(rol)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return "Exito"
    
    def buscarPorNombreRol(self,nombre):
        return db.session.query(Rol).filter(Rol.nombre.ilike("%"+nombre+"%")).all()