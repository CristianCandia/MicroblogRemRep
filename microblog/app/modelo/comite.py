"""
@organization: Sigma-System - CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
"""

"""Se importa el modulo para el manejo de la base de datos"""
from app import db

usr_por_comite = db.Table('usr_comite', 
                             db.Column('id', db.Integer, primary_key = True),
                             db.Column('id_comite', db.Integer, db.ForeignKey('comite.id')),
                             db.Column('id_usr', db.Integer, db.ForeignKey('user2.id'))
                            )
"""@note: Clase que representa al usuario"""
class Comite(db.Model):
    
    """Id que se le asigna al comite"""
    id = db.Column(db.Integer, primary_key = True)
    
    """Define el nombre del comite"""
    nombre = db.Column(db.String(64))
    
    """Almacena la cantidad de miembros del comite"""
    cant_miembros = db.Column(db.Integer)
    
    
    """Define el proyecto al que pertenece"""
    id_proyecto = db.Column(db.Integer)
    
       
    """registra el rol asociado al usuario"""
    
    usuarios = db.relationship('User2', secondary = usr_por_comite, 
                            backref = db.backref('comites', lazy = 'dinamic'))
    
    """@note: Metodo para agregar comite"""
    def add_comite(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
        
    """
        @note: Metodo para eliminar un comite
        @return: Retorna un mensaje  de confirmacion o error
    """
    def delete_comite(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
    
    """
        @note: Metodo que devuelve el id de un comite
        @return: Retorna un string id
    """
    def get_id(self):
        return unicode(self.id)
    
    """
        @note: Metodo que imprime el nombre que representa al objeto
        @return: Retorna un nombre de objeto
    """
    def __repr__(self):
        return '<User %r>' % (self.nombre)
