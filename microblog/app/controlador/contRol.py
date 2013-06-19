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
    
    def cargarPermisos(self):
        lista = []
        p1 = {'id': 'u1','nombre':'Crear usuario','check':''}
        lista.append(p1)
        p2 = {'id': 'u2','nombre':'Modificar usuario','check':''}
        lista.append(p2)
        p3 = {'id': 'u3','nombre':'Eliminar usuario','check':''}
        lista.append(p3)
        p4 = {'id': 4,'nombre':'Crear rol','check':''}
        lista.append(p4)
        p5 = {'id': 5,'nombre':'Modificar rol','check':''}
        lista.append(p5)
        p6 = {'id': 6,'nombre':'Eliminar rol','check':''}
        lista.append(p6)
        p7 = {'id': 7,'nombre':'Asignar rol','check':''}
        lista.append(p7)
        p8 = {'id': 8,'nombre':'Crear proyecto','check':''}
        lista.append(p8)
        p9 = {'id': 9,'nombre':'Configurar proyecto','check':''}
        lista.append(p9)
        p10 = {'id': 10,'nombre':'Modificar proyecto','check':''}
        lista.append(p10)
        p11 = {'id': 11,'nombre':'Eliminar proyecto','check':''}
        lista.append(p11)
        p12 = {'id': 12,'nombre':'Ver fase','check':''}
        lista.append(p12)
        p13 = {'id': 13,'nombre':'Crear item','check':''}
        lista.append(p13)
        p14 = {'id': 14,'nombre':'Eliminar item','check':''}
        lista.append(p14)
        p15 = {'id': 15,'nombre':'Modificar item','check':''}
        lista.append(p15)
        p16 = {'id': 16,'nombre':'Crear tipo de item','check':''}
        lista.append(p16)
        p17 = {'id': 17,'nombre':'Modificar item','check':''}
        lista.append(p17)
        p18 = {'id': 18,'nombre':'Eliminar tipo de item','check':''}
        lista.append(p18)
        p19 = {'id': 19,'nombre':'Crear linea base','check':''}
        lista.append(p19)
        p20 = {'id':20,'nombre':'Liberar-cerrar linea base','check':''}
        lista.append(p20)
        p21 = {'id': 21,'nombre':'Eliminar Linea base','check':''}
        lista.append(p21)
        p22 = {'id': 22,'nombre':'Aprobar-rechazar item','check':''}
        lista.append(p22)
        p23 = {'id': 23,'nombre':'Solicitar reportes','check':''}
        lista.append(p23)
        p24 = {'id': 24,'nombre':'Aprobar-rechazar solicitud de cambio','check':''}
        lista.append(p24)
        return lista
    
    def getPermisos_X_Rol(self,idr):
        permisosAux = self.cargarPermisos()
        permisos = self.getRol(idr).permisos
        for p in permisos:
            permisosAux[p.id-1]['check']='checked'
            print 
        return permisosAux
    
    def getlistaPermisos(self):
        p = {}
        p['id']=90
        p['state']='false'
        p['nombre'] = 'prueba'
        lista = []
        lista.append(p)
        pass
    
    def getRol(self,idr):
        return Rol.query.get(idr)
    
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