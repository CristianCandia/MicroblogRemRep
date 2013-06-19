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
    """
        Atributos que relacionan la fase con el tipo de item.
    """
    
def codigoTI(id_Proyecto, id_Fase, numeroItem):
    cod = "SS" + str(id_Proyecto) + "_F" + str(id_Fase) + "_I" + str(numeroItem)
    return cod
    
###############################################################################
###############################################################################
###############################################################################

relacion_item = db.Table('relacion_item',
                         db.Column('id', db.Integer,
                                   primary_key = True),
                         db.Column('id_item', db.Integer,
                                   db.ForeignKey('item.id_item')),
                         db.Column('id_relacion', db.Integer,
                                   db.ForeignKey('relacion.id_relacion')))
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
    """
    
    estado = db.Column(db.String(64))
    """
        Atributo que define el estado en que se encuentra el 
        item.
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

###############################################################################
###############################################################################
###############################################################################


class Relacion(db.Model):
    """
        Definicion de la entidad relacion
    """
    id_relacion = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(Enum('Antecesor', 'Padre', name = 'tipo_relacion'))
    id_item = db.Column(db.Integer, db.ForeignKey('item.id_item'))
    
    def __repr__(self):
        return '<Relacion %r>' % (self.id_item)
