'''
Created on 02/05/2013

@author: cristian
'''
"""
Sygma_System
:organization:CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
models.py
"""
from app import db
""":note: Clase que representa al usuario"""
class Proyecto(db.Model):
    """Id que se le asigna al usuario"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nombre del proyecto"""
    nombre = db.Column(db.String(64), index = True, unique = True)
    """Indica la descripcion del proyecto"""
    descripcion = db.Column(db.String(120), nullable = False)
    """Registra la fecha de creacion del proyecto"""
    fecha_de_creacion = db.Column(db.Date)
    """Registra la complejidad total del proyecto"""
    complejidad_total = db.Column(db.Integer)
    """Indica el estado actual del proyecto"""
    estado = db.Column(db.String(50))
  
    def add_proy(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
    
    """Imprime el titulo del proyecto"""
    def __repr__(self):
        return '<<Proyecto %r>'%(self.nombre)