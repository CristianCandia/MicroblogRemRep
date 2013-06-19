"""
Sygma_System
:organization:CRF_Proyect
:author:Cristian Candia
:author:Ruth Centurion
:author:Fernando Saucedo

forms.py
"""
from flask.ext.wtf import Form, TextField, PasswordField, DateField, IntegerField, BooleanField
from flask.ext.wtf import Required, widgets, SelectMultipleField

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
    idProy = IntegerField('idProy')
    nomProy = TextField('nombre', validators = [Required()])
    descripcion = TextField('desc')
    fecha_de_creacion = DateField('fecha')
    complejidad = IntegerField('complejidad')
    estado = TextField('estado')

class fase_CrearForm(Form):
    idFase = IntegerField('idFase')
    nomFase = TextField('nomFase', validators = [Required()])
    posicion = IntegerField('posicion', validators = [Required()])
    descripcion = TextField('descripcion')
    cantidadItems = IntegerField('cantidadItems')
    cantidadLB = IntegerField ('cantidadLB')
    estado = TextField('estado')
    idProy = IntegerField('idProy')
    
class rol_CrearForm(Form):
    idRol = IntegerField('idRol')
    nomRol = TextField('nombre', validators = [Required()])
    descripcion = TextField('descripcion')
    idUsr = IntegerField('idUsr')

class permiso_CrearForm(Form):
    nombre = TextField('nombre', validators = [Required()])
    codigo = TextField('codigo', validators = [Required()])

class asignar_Permisos(Form):
    id_rol = IntegerField('id_rol')
    id_permiso = IntegerField ('id_permiso')
    
    
class asignar_Roles(Form):
    id_usr = IntegerField('id_usr')
    id_rol = IntegerField ('id_rol')
    
class buscar(Form):
    nombreBuscado = TextField('nombre-buscado')
    
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(Form):
    string_of_files = ['one\r\ntwo\r\nthree\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)

class listarPermisos(Form):
    u1 = BooleanField()
    u2 = BooleanField()
    u3 = BooleanField()
    u4 = BooleanField()
    u5 = BooleanField()
    u6 = BooleanField()
    u7 = BooleanField()
    u8 = BooleanField()
    u9 = BooleanField()
    u10 = BooleanField()
    u11 = BooleanField()
    u12 = BooleanField()
    u13 = BooleanField()
    u14 = BooleanField()
    u15 = BooleanField()
    u16 = BooleanField()
    u17 = BooleanField()
    u18 = BooleanField()
    u19 = BooleanField()
    u20 = BooleanField()
    u21 = BooleanField()
    u22 = BooleanField()
    u23 = BooleanField()
    u24 = BooleanField()