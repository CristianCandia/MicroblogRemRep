'''
Created on 02/05/2013

@author: cristian
'''
from app.modelo import Fase
from app.controlador import ControllerProy
from app import db
class ControllerFase():
    def regFase(self, **kwargsProy):
        fase = Fase()
        for k, v in kwargsProy.iteritems():
            if k == 'nombre':
                fase.nombre = v
            if k == 'posicion':
                fase.posicion = v
            if k == 'descripcion':
                fase.descripcion = v
            if k == 'cantidadItems':
                fase.cantidadItems = v
            if k == 'cantidadLB':
                fase.cantidadLB = v
            if k == 'estado':
                fase.estado = v
            if k == 'idProy':
                fase.id_proyecto = v
            
        return fase.add_fase()
    
    def getFase(self, idfase):
        return Fase.query.get(idfase)
    
    def traerFases(self):
        return Fase.query.all()
    
    def modFase(self, faseAux):
        fase = self.getFase(faseAux.id)
        fase.nombre = faseAux.nombre
        fase.posicion = faseAux.posicion
        fase.descripcion = faseAux.descripcion
        fase.cantidadItems = faseAux.cantidadItems
        fase.cantidadLB = faseAux.cantidadLB
        fase.estado = faseAux.estado
        try:
            db.session.merge(fase)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return "Exito"
    
    def eliminarFase(self, fase):
        return fase.delete_fase()
    
    def buscarPorNombreFaseProyecto(self,nombre,idp):
        fasesAux = db.session.query(Fase).filter(Fase.nombre.ilike("%"+nombre+"%")).all()
        fases = []
        #fasesAux = db.session.query(Fase).filter(Fase.nombre.ilike(nombre), Fase.id_proyecto.ilike(idp)).all()
        if fasesAux != None:
            for f in fasesAux:
                if f.id_proyecto == idp:
                    fases.append(f)
            return fases