"""
@organization: Sigma-System - CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
"""

from app import db
"""@note: Clase que representa a los permisos"""
class Permiso(db.Model):
    """Id que se le asigna a un permiso especifico"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nombre del permiso"""
    nombre = db.Column(db.String(64))
    """Registra el codigo del permiso"""
    codigo = db.Column(db.String(64))
    
    """
        @note: Metodo para agregar un permiso
        
    """
    def add_permiso(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
        
    """
        @note: Metodo que imprime el nombre que representa al objeto
        @return: Retorna un nombre de objeto
    """
    def __repr__(self):
        return '<Permiso %r>' % (self.nombre)
