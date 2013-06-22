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
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

class AtributoPorTI(db.Model):
    """
        Clase que representa a la Entidad Atributo por TI.
    """
    __tablename__ = 'atributo_TI'
    id_Atrib_TI = db.Column(db.Integer, primary_key = True)
    """
        Clave primaria de la clase.        
    """
    
    id_TI = db.Column(Integer, ForeignKey('tipo_item.id_TI'), nullable = False)
    """
        Atributo que enlaza un tipo de item con su atributo.
        
    """
    
    nombre = Column(String(64))
    
    tipo = Column(String(64))
    
    valorDefault = Column(String(100))
    
    
    
    def __init__(self, idTI, nombre, tipo, valorDefault):
        """
            Constructor de la calse AtributoPorTI
            @param idTI: Id del TI asociado
            @param nombre: Nombre del Atributo
            @param tipo: Tipo del Atributo
            @param valorDefault: Valor por defecto del Atributo
        """
        self.id_TI = idTI
        self.nombre = nombre
        self.tipo = tipo
        self.valorDefault = valorDefault
    
###############################################################################
###############################################################################
###############################################################################

class AtributoPorItem(Model):
    """
        Clase que representa a la Entidad Atributo por Item.
    """
    
    id_Atrib_Item = db.Column(db.Integer, primary_key = True)
    """
        Clave primaria de la clase.
    """
    
    id_Item = Column(Integer, ForeignKey('Item.id_Item'), nullable = False)
    
    id_Atrib_TI = Column(Integer, ForeignKey('atributo_TI.id_Atrib_TI'), nullable = False)
    
    valor = Column(String(100))

