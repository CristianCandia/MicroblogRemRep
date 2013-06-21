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
    
    def getRolIdf(self, idf):
        return Rol.query.filter_by(id_fase = idf).all()
    
    def cargarPermisos(self):
        lista = []
        p1 = {'nom': 'u1','nombre':'Crear usuario','check':'', 'id':1}
        lista.append(p1)
        p2 = {'nom': 'u2','nombre':'Modificar usuario','check':'','id':2}
        lista.append(p2)
        p3 = {'nom': 'u3','nombre':'Eliminar usuario','check':'','id':3}
        lista.append(p3)
        p4 = {'nom': 'u4','nombre':'Crear rol','check':'','id':4}
        lista.append(p4)
        p5 = {'nom': 'u5','nombre':'Modificar rol','check':'','id':5}
        lista.append(p5)
        p6 = {'nom': 'u6','nombre':'Eliminar rol','check':'','id':6}
        lista.append(p6)
        p7 = {'nom': 'u7','nombre':'Asignar rol','check':'','id':7}
        lista.append(p7)
        p8 = {'nom': 'u8','nombre':'Crear proyecto','check':'','id':8}
        lista.append(p8)
        p9 = {'nom': 'u9','nombre':'Configurar proyecto','check':'','id':9}
        lista.append(p9)
        p10 = {'nom': 'u10','nombre':'Modificar proyecto','check':'','id':10}
        lista.append(p10)
        p11 = {'nom': 'u11','nombre':'Eliminar proyecto','check':'','id':11}
        lista.append(p11)
        p12 = {'nom': 'u12','nombre':'Ver fase','check':'','id':12}
        lista.append(p12)
        p13 = {'nom': 'u13','nombre':'Crear item','check':'','id':13}
        lista.append(p13)
        p14 = {'nom': 'u14','nombre':'Eliminar item','check':'','id':14}
        lista.append(p14)
        p15 = {'nom': 'u15','nombre':'Modificar item','check':'','id':15}
        lista.append(p15)
        p16 = {'nom': 'u16','nombre':'Crear tipo de item','check':'','id':16}
        lista.append(p16)
        p17 = {'nom': 'u17','nombre':'Modificar item','check':'','id':17}
        lista.append(p17)
        p18 = {'nom': 'u18','nombre':'Eliminar tipo de item','check':'','id':18}
        lista.append(p18)
        p19 = {'nom': 'u19','nombre':'Crear linea base','check':'','id':19}
        lista.append(p19)
        p20 = {'nom': 'u20','nombre':'Liberar-cerrar linea base','check':'','id':20}
        lista.append(p20)
        p21 = {'nom': 'u21','nombre':'Eliminar Linea base','check':'','id':21}
        lista.append(p21)
        p22 = {'nom': 'u22','nombre':'Aprobar-rechazar item','check':'','id':22}
        lista.append(p22)
        p23 = {'nom': 'u23','nombre':'Solicitar reportes','check':'','id':23}
        lista.append(p23)
        p24 = {'nom': 'u24','nombre':'Aprobar-rechazar solicitud de cambio','check':'', 'id':24}
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
    
    def asignarDesasginarPer(self, id_rol, permisos):
        c_permiso = ControllerPermiso()
        permisos2 = self.getRol(id_rol).permisos
        respuesta = []
        for p in permisos:
            perm = c_permiso.getPermiso(p['id'])
            if not perm in permisos2 and p['dato']:
                temp = self.asignarPermisos(id_rol, perm.id)
                if temp == 'Exito':
                    respuesta.append({'error':0,'id':perm.id,'obs':temp})
                else:
                    respuesta.append({'error':1,'id':perm.id,'obs':temp})
        
        for p in permisos:
            if not (p['dato']):
                perm = c_permiso.getPermiso(p['id'])
                if perm in permisos2:
                    temp = self.desasignarPermisos(id_rol, perm.id)
                    if temp == 'Exito':
                        respuesta.append({'error':0,'id':perm.id,'obs':temp})
                    else:
                        respuesta.append({'error':2,'id':perm.id,'obs':temp})
                        
        
        return respuesta  
            
        #if perm in permisos2:
        #    print "Existe este permiso"
        #else:
        #    print "No existe este permiso"    
        
        #for p in permisos2:
            #print p
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
    
    def desasignarPermisos(self,id_rol,id_permiso):
        c_permiso = ControllerPermiso()
        rol = self.getRol(id_rol)
        permiso = c_permiso.getPermiso(id_permiso)
        
        if rol != None and permiso != None:
            rol.permisos.remove(permiso)
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