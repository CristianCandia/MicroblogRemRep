"""
Sygma_System
:organization:CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
models.py
"""
from app import db
""":note: Clase que representa a la fase"""
class Fase(db.Model):
    """Id que se le asigna a la fase"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nombre de la fase"""
    nombre = db.Column(db.String(64))
    """Registra la posicion de la fase en el proyecto"""
    posicion = db.Column(db.Integer)
    """Registra la descripcion de la fase"""
    descripcion = db.Column(db.String(120))
    """Registra la cantidad de items de la fase"""
    cantidadItems = db.Column(db.Integer)
    """Registra la cantidad de linea base de una base"""
    cantidadLB = db.Column(db.Integer)
    """Registra el estado de una fase"""
    estado = db.Column(db.String(64))
    
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyecto.id'))

    
    def add_fase(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
        
    
    def __repr__(self):
        return '<Fase %r>' % (self.nombre)
    
    def delete_fase(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"