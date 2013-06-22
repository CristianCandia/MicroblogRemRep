"""
@organization: Sigma-System - CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
"""

from app import db
"""@note: Clase que representa a la fase"""
class Solicitud(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(64))
    impacto_total = db.Column(db.String(50))
    costo_total = db.Column(db.Integer)
    estado = db.Column(db.String(50))
    id_comite = db.Column(db.Integer, db.ForeignKey('comite.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('user2.id'))
    cantidad_votos = db.Column(db.Integer)
    
    """
        @note: Metodo para agregar una fase
    """
    def add_solicitud(self):
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
        return '<Fase %r>' % (self.nombre)
    
    """
        @note: Metodo para eliminar una fase        
        @return: Retorna un mensaje  de confirmacion o error
    """
    def delete_solicitud(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
