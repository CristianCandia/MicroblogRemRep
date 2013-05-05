"""
Sygma_System
:organization:CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
models.py
"""
from app import db

permiso_por_rol = db.Table('permiso_rol',
    db.Column('id', db.Integer, primary_key = True),
    db.Column('id_rol', db.Integer, db.ForeignKey('rol.id')),
    db.Column('id_permiso', db.Integer, db.ForeignKey('permiso.id'))
)
""":note: Clase que representa a los roles"""
class Rol(db.Model):
    """Id que se le asigna a un rol especifico"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nombre del rol"""
    nombre = db.Column(db.String(64))
    """Registra la descripcion del rol"""
    descripcion = db.Column(db.String(120))
    
    permisos = db.relationship('Permiso', secondary = permiso_por_rol,
        backref = db.backref('roles', lazy='dynamic'))
    
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyecto.id'))
    
    id_fase = db.Column(db.Integer, db.ForeignKey('fase.id'))
    
    def add_rol(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
        
    
    def __repr__(self):
        return '<Rol %r>' % (self.nombre)