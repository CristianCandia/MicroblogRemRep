'''
Created on 02/05/2013

@author: cristian
'''
from app.modelo import Fase
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
        return fase.add_fase()
    def traerFases(self):
        return Fase.query.all()