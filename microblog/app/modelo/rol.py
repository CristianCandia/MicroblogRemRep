"""
Sygma_System
:organization:CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
models.py
"""
from app import db
""":note: Clase que representa a los roles"""
class Rol(db.Model):
    """Id que se le asigna a un rol especifico"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nombre del rol"""
    nombre = db.Column(db.String(64))
    """Registra la descripcion del rol"""
    descripcion = db.Column(db.String(120))
    
    def add_rol(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
        
    
    def __repr__(self):
        return '<Rol %r>' % (self.nombre)