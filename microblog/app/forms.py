"""
Sygma_System
:organization:CRF_Proyect
:author:Cristian Candia
:author:Ruth Centurion
:author:Fernando Saucedo

forms.py
"""
from flask.ext.wtf import Form, TextField, PasswordField, DateField, IntegerField
from flask.ext.wtf import Required

""":note: Clase de Formulario de Login"""
class LoginForm(Form):
    nomUsr = TextField('openid', validators = [Required()])
    passWord = PasswordField('password', validators = [Required()])

class usr_CrearForm(Form):
    nomUsr = TextField('nombre', validators = [Required()])
    passWord = PasswordField('password', validators = [Required()])
    
class proy_CrearForm(Form):
    nomProy = TextField('nombre', validators = [Required()])
    descripcion = TextField('desc')
    fecha_creacion = DateField('fecha')
    complejidad = IntegerField('complejidad')
    estado = TextField('estado')   