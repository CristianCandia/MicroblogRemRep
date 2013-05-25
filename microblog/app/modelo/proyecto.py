"""
@organization: Sigma-System - CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
"""
from app import db
"""@note: Clase que representa al proyecto"""
class Proyecto(db.Model):
    """Id que se le asigna al usuario"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nombre del proyecto"""
    nombre = db.Column(db.String(64), index = True, unique = True)
    """Indica la descripcion del proyecto"""
    descripcion = db.Column(db.String(120), nullable = False)
    """Registra la fecha de creacion del proyecto"""
    fecha_de_creacion = db.Column(db.Date)
    """Registra la complejidad total del proyecto"""
    complejidad_total = db.Column(db.Integer)
    """Indica el estado actual del proyecto"""
    estado = db.Column(db.String(50))
    
    fases = db.relationship('Fase', backref='proyecto',lazy='dynamic')
    
    """
        @note: Metodo para agregar un permiso
    """
    def add_proy(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
    """
        @note: Metodo para eliminar un proyecto        
        @return: Retorna un mensaje  de confirmacion o error
    """
    def delete_proyecto(self):
        try:
            db.session.delete(self)
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
        return '<<Proyecto %r>'%(self.nombre)
