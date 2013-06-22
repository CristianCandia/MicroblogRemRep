"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from app import db
from flask_sqlalchemy import Model
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer

class LineaBase(db.Model):
    """
        Clase que representa a la entidad linea_base
    """
    
    __tablename__ = 'linea_base'
    
    id = db.Column(db.Integer, primary_key = True)
    """
        Clave primaria de la entidad.
    """
    
    nombre = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    fecha_creacion = db.Column(db.Date) 

    fase_id = db.Column(None, db.ForeignKey("fase.id"), nullable=True)
    fase = db.relation('Fase', backref=db.backref('fase_LB'))
    
class ItemsPorLineaBase(db.Model):
    """
        Clase que representa a la entidad items_x_LB
    """
    __tablename__ = 'items_x_LB'
    
    id = db.Column(db.Integer, primary_key = True)
    """
    
    """
    
    id_item = db.Column(db.Integer, db.ForeignKey('item.id_item'))
    """
    
    """
    
    id_linea_base = db.Column(db.Integer, db.ForeignKey('linea_base.id'))
    """
    
    """