"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from app import db


class HistorialItem(db.Model):
    """
        Clase que representa a la entidad historial_item.
    """
    
    __tablename__ = 'historial_item'
    
    id_historial_item = db.Column(db.Integer, primary_key = True)
    """
        Clave primaria de la entidad.
    """
    
    tipoModificacion = db.Column(db.String(100))
    
    fechaModificacion = db.Column(db.Date)
    
    id_item = db.Column(db.Integer, db.ForeignKey('item.id_item'))
    
    id_usuario = db.Column(db.Integer, db.ForeignKey('user2.id'))
    
class HistorialLineaBase(db.Model):
    
    __tablename__ = 'historial_relacion'
    
    id = db.Column(db.Integer, primary_key = True)
    
    id_lb = db.Column(None, db.ForeignKey("linea_base.id"), nullable=True)
    operacion = db.Column(db.String(100))
    id_usuario = db.Column(db.Integer, db.ForeignKey('user2.id'))
    fecha = db.Column(db.Date)