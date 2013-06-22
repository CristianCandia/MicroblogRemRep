"""
@organization: Sigma-System - CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
"""

from app import db
"""@note: Clase que representa a los permisos"""
class Voto(db.Model):
    """Id que se le asigna a un permiso especifico"""
    id = db.Column(db.Integer, primary_key = True)
    id_solicitud =  db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    voto = db.Column(db.Integer)
    
    def add_voto(self):
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
