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
    
class rec_passForm(Form):
    nomUsr = TextField('name', validators = [Required()])

class usr_CrearForm(Form):
    nomUsr = TextField('nick', validators = [Required()])
    passWord = PasswordField('password', validators = [Required()])
    nombre =  TextField('nombre', validators = [Required()])
    apellido = TextField('apellido', validators = [Required()])
    telefono = TextField('telefono', validators = [Required()])
    ci = TextField('ci', validators = [Required()])
    e_mail = TextField('e_mail', validators = [Required()])

class proy_CrearForm(Form):
    nomProy = TextField('nombre', validators = [Required()])
    descripcion = TextField('desc')
    fecha_creacion = DateField('fecha')
    complejidad = IntegerField('complejidad')
    estado = TextField('estado')

class fase_CrearForm(Form):
    nombre = TextField('nombre', validators = [Required()])
    posicion = IntegerField('posicion', validators = [Required()])
    descripcion = TextField('descripcion')
    cantidadItems = IntegerField('cantidadItems')
    cantidadLB = IntegerField ('cantidadLB')
    estado = TextField('estado')
    
class rol_CrearForm(Form):
    nombre = TextField('nombre', validators = [Required()])
    descripcion = TextField('descripcion')

class permiso_CrearForm(Form):
    nombre = TextField('nombre', validators = [Required()])
    codigo = TextField('codigo', validators = [Required()])

class asignar_Permisos(Form):
    id_rol = IntegerField('id_rol')
    id_permiso = IntegerField ('id_permiso')
    
    
class asignar_Roles(Form):
    id_usr = IntegerField('id_usr')
    id_rol = IntegerField ('id_rol')