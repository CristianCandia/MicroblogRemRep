'''
Created on 02/05/2013

@author: cristian
'''
from app.modelo import Proyecto
class ControllerProy():
    def regProyecto(self, **kwargsProy):
        proy = Proyecto()
        for k, v in kwargsProy.iteritems():
            if k == 'nombre':
                proy.nombre = v
            if k == 'descripcion':
                proy.descripcion = v
            if k == 'fecha_de_creacion':
                proy.fecha_de_creacion = v
            if k == 'complejidad_total':
                proy.complejidad_total = v
            if k == 'estado':
                proy.estado = v
        return proy.add_proy()
    
    def getNombre(self, id):
        p = Proyecto.query.get(id)
        return p.nombre
    
    def getProy(self, id):
        return Proyecto.query.get(id)
    
    def traerProyectos(self):
        return Proyecto.query.all()
    
    def modProyecto(self, proyecto):
        try:
            db.session.merge(proyecto)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
    
    def eliminarProyecto(self, proyecto):
        return proyecto.delete_proyecto()