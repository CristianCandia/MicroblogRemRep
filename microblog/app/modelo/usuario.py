"""
Sygma_System
:organization:CRF_Proyect
@author: Cristian Candia
@author: Ruth Centurion
@author: Fernando Saucedo
models.py
"""
from app import db
ROLE_USER = 0
ROLE_ADMIN = 1

rol_por_usuario = db.Table('rol_usuario', 
                             db.Column('id', db.Integer, primary_key = True),
                             db.Column('id_usuario', db.Integer, db.ForeignKey('user2.id')),
                             db.Column('id_rol', db.Integer, db.ForeignKey('rol.id'))
                            )
""":note: Clase que representa al usuario"""
class User2(db.Model):
    """Id que se le asigna al usuario"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nickname del usuario"""
    name = db.Column(db.String(64), index = True, unique = True)
    """almacena el password del user"""
    passWord = db.Column(db.String(120), index = True, unique = True)
    """Define el nombre del usuario"""
    nombre = db.Column(db.String(64))
    """Define el apellido del usuario"""
    apellido = db.Column(db.String(64))
    """Define el telefono del usuario"""
    telefono = db.Column(db.String(15))
    """Registra el documento del usuario"""
    ci = db.Column(db.String(15))
    """Almacena una direccion de correo elec del usuario"""
    e_mail = db.Column(db.String(15), unique = True)
    
    """registra el rol asociado al usuario"""
    #roles = db.Column(db.SmallInteger, default = ROLE_USER)
    roles = db.relationship('Rol', secondary = rol_por_usuario, 
                            backref = db.backref('usuarios', lazy = 'dinamic'))
    
    def add_usr(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, error :
            db.session.rollback()
            return str(error)
        return "Exito"
        
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return '<User %r>' % (self.name)