'''
Created on 01/05/2013

@author: cristian
'''
from app import db
from app.modelo import User2
from contRol import ControllerRol
class ControllerUsr():
    def regUsuario(self, **kwargsUsr):
        usr = User2()
        for k, v in kwargsUsr.iteritems():
            if k == 'name':
                usr.name = v
            if k == 'passWord':
                usr.passWord = v
            if k == 'nombre':
                usr.nombre = v
            if k == 'apellido':
                usr.apellido = v
            if k == 'telefono':
                usr.telefono = v
            if k == 'ci':
                usr.ci = v
            if k == 'e_mail':
                usr.e_mail = v
        return usr.add_usr()
    
    def getUsr(self, id):
        return User2.query.get(id)
    
    def getUsrName(self, name):
        return User2.query.filter_by(name = name).first()
    
    def getUsrFull(self):
        return User2.query.all()
    
    def getRoles(self,idu):
        return self.getUsr(idu).roles
    
    def asignarRolAListaDeUsr(self,usr,idr):
        for u in usr:
            resp = self.asignarRoles(u, idr)
        return resp
    
    def asignarRoles(self,id_usr,id_rol):
        c_rol = ControllerRol()
        
        usr = self.getUsr(id_usr)
        rol = c_rol.getRol(id_rol)
        
        if usr != None and rol != None:
            usr.roles.append(rol)
            try:
                db.session.merge(rol)
                db.session.commit()
            except Exception, error:
                db.session.rollback()
                return error
            return 'Exito'
        return 'No existen el/los id(s) ingresados'
    
    def modUsuario(self, usuario):
        try:
            db.session.merge(usuario)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
    
    def eliminarUsr(self, usuario):
        return usuario.delete_usr()
    
    def getPermisos(self, usr):
        sopermi = []
        if usr.roles is not None:
            for rol in usr.roles:
                if rol.permisos is not None:
                    for p in rol.permisos:
                        if not p.id in sopermi:
                            sopermi.append(p.id)
        return sopermi

    def buscarPorNombreUsuario(self,nombre):
        return db.session.query(User2).filter(User2.name.ilike("%"+nombre+"%")).all()