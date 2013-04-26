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
""":note: Clase que representa al usuario"""
class User(db.Model):

    """Id que se le asigna al usuario"""
    id = db.Column(db.Integer, primary_key = True)
    """Define el nickname del usuario"""
    name = db.Column(db.String(64), index = True, unique = True)
    """almacena el password del user"""
    passWord = db.Column(db.String(120), index = True, unique = True)
    """registra el rol asociado al usuario"""
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    
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