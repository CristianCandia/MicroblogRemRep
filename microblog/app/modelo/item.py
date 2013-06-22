"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""


from app import db
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum

ROLE_USER = 0
ROLE_ADMIN = 1

###############################################################################
###############################################################################
###############################################################################

Herencia_TipoItem = db.Table('herencia_TI',
                             db.Column('id', db.Integer, primary_key = True),
                             db.Column('padre', db.Integer, 
                                       db.ForeignKey('tipo_item.id_TI')),
                             db.Column('hijo', db.Integer, 
                                       db.ForeignKey('tipo_item.id_TI')))
"""
    Entidad para realizar la herencia entre TIs
"""

###############################################################################
###############################################################################
###############################################################################

class TipoItem(db.Model):
    """
        @note: Clase que representa a la Entidad Tipo de Item.
    """
    __tablename__ = 'tipo_item'
    id_TI = db.Column(db.Integer, primary_key = True)
    """
        Clave primaria de la tabla.
    """
    
    codigo = db.Column(db.String(100))
    
    nombre_TI = db.Column(db.String(100))
    """
        Atributo que representa el codigo del tipo de item.
    """
    
    descripcion = db.Column(db.String(100))
    """
        Atributo que describe al tipo de item.
    """
    
    proyecto_id = db.Column(None, db.ForeignKey("proyecto.id"), nullable=True)
    proyecto = db.relation('Proyecto', backref=db.backref('proyecto'))
    """
        Atributos que relacionan el proyecto con el tipo de item.
    """
    
    fase_id = db.Column(None, db.ForeignKey("fase.id"), nullable=True)
    fase = db.relation('Fase', backref=db.backref('fase'))
    
    items = db.relation('Item', backref=db.backref('item'))
    """
        Atributos que relacionan la fase con el tipo de item.
    """
    
    def __init__(self, codigo, nombre_TI, descripcion, proyecto_id, 
                 fase_id):
        """
            Constructor de la clase TipoItem
            @param codigo: codigo con el que le registra el sistema al TI
            @param nombre_TI: nombre que le asigna el usuario
            @param descripcion: descripcion del TI
            @param proyecto_id: id del proyecto asociado
            @param fase_id: id de la fase asociada
        """
        self.codigo = codigo
        self.nombre_TI = nombre_TI
        self.descripcion = descripcion
        self.proyecto_id = proyecto_id
        self.fase_id = fase_id
    
###############################################################################
###############################################################################
###############################################################################

relacion_item = db.Table('relacion_item',
                         db.Column('id', db.Integer,
                                   primary_key = True),
                         db.Column('id_item_1', db.Integer,
                                   db.ForeignKey('item.id_item')),
                         db.Column('id_item_2', db.Integer,
                                   db.ForeignKey('item.id_item')),
                         db.Column('relacion', db.Integer))
"""Definicion de la entidad relaciones"""

###############################################################################
###############################################################################
###############################################################################

class Item(db.Model):
    """
        @note: Clase que representa a la entidad Item
    """
    
    id_item = db.Column(db.Integer, primary_key = True)
    """
        Id asignado a cada item del proyecto
    """
    
    descripcion = db.Column(db.String(200))
    """
        Atributo para dar una descripcion sobre el item
    """
    
    numero = db.Column(db.Integer)
    """
        Atributo para saber cantidad de items por fase
    """
    
    num_x_TI = db.Column(db.Integer)
    """
        Atributo para saber cantidad de items de ese tipo de item
         por fase
    """
    
    id_TI = db.Column(db.Integer, db.ForeignKey('tipo_item.id_TI'))
    """
        Atributo para definir el tipo de item
    """
    
    id_fase = db.Column(db.Integer, db.ForeignKey('fase.id'))
    """
        Atributo que define la fase a la que pertenece ese item
    """
    
    version = db.Column(db.Integer)
    """
        Atributo que define la version del item.
    """
    
    complejidad = db.Column(db.Integer)
    """
        Atributo que define la complejidad del item. 
    """
    
    prioridad = db.Column(db.Integer)
    """
        Atributo que define la prioridad del item.
        1. Alta.
        2. Media.
        3. Baja
    """
    
    estado = db.Column(db.Integer)
    """
        Atributo que define el estado en que se encuentra el 
        item.
        1 = Aprobado.
        2 = Desaprobado.
        3 = Bloqueado.
        4 = Revision-Bloqueada.
        5 = Revision-Desbloqueada
        6 = Finalizada
    """
    
    borrado = db.Column(db.Boolean)
    """
        Atributo que indica el borrado logico del item.
    """
    
    observaciones = db.Column(db.String(200))
    """
        Atributo que define las observaciones correspondientes al item.
    """
    
    relacion = db.relationship('Relacion', secondary = relacion_item, 
                            backref = db.backref('item', lazy = 'dinamic'))
    
    
    def __repr__(self):
        """
            @note: Metodo que imprime el nombre que representa al objeto
        """
        return '<Item %r>' % (self.descripcion)