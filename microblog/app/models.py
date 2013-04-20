'''
Created on 19/04/2013

@author: cristian
'''
from app import db
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    """Clase que representa a User"""
    id = db.Column(db.Integer, primary_key = True)
    """:var id: Id que se le asigna al usuario"""
    name = db.Column(db.String(64), index = True, unique = True)
    """:var name: Define el nickname del usuario"""
    passWord = db.Column(db.String(120), index = True, unique = True)
    """:var passWord: almacena el password del user"""
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    """:var role: registra el rol asociado al usuario"""
    
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
