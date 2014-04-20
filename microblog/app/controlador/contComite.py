"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""
"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from app.modelo import Comite, User2
from app import db

class ControllerComite():
    def regComite(self, **kwargsProy):
        comite = Comite()
        for k, v in kwargsProy.iteritems():
            if k == 'nombre':
                comite.nombre = v
            if k == 'cant_miembros':
                comite.cant_miembros = v
            if k == 'id_proyecto':
                comite.id_proyecto = v
        return comite.add_comite()
    
    def asignarComiteAListaDeUsr(self,lista_idu,idc):
        for u in lista_idu:
            resp = self.asignarComite(u, idc)
        return resp
    
    def asignarComite(self,usr,id_com):
        com = self.getComite(id_com)
        user = User2.query.get(usr)
        if user != None and com != None:
            com.usuarios.append(user)
            try:
                db.session.merge(com)
                db.session.commit()
            except Exception, error:
                db.session.rollback()
                return error
            return 'Exito'
        return 'No existen el/los id(s) ingresados'
    
    def getComiteXIdp(self,idp):
        return Comite.query.filter_by(id_proyecto = idp).first()
    
    def usrSinComiteIdc(self, idc):
        usuarios2 = []
        usuarios = User2.query.all()
        comite = self.getComite(idc)
        for u in usuarios:
            if not (u in comite.usuarios):
                usuarios2.append(u)
        return usuarios2
    
    def hayComite(self, idp = None):
        com = Comite.query.filter_by(id_proyecto = idp).first()
        if com != None:
            return 1
        else:
            return 0
    def getComites(self):
        return Comite.query.all()
    
    def getComite(self, id_comite):
        return Comite.query.get(id_comite)   