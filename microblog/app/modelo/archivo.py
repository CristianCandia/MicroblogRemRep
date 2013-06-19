"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from app import db
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship

class Archivo (db.Model):
    """
        Clase que representa a la entidad Archivo
    """
    __tablename__ = "archivo"
    id = db.Column(db.Integer, primary_key=True)
    datos = db.Column(db.Binary)
    nombre = db.Column(db.String)
    tipo = db.Column(db.String)
    id_item = db.Column(db.Integer, ForeignKey('item.id_item'))
    activo = db.Column(db.Boolean)
    relationship('item')

    def __init__(self, nombre, datos, tipo, id_item, activo):
        self.datos = datos;
        self.nombre = nombre;
        self.tipo = tipo
        self.id_item = id_item
        self.activo = activo
        
        
    def __repr__(self):
        return '<User %r>' % (self.nombre)