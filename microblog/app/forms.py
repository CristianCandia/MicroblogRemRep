"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from flask.ext.wtf import Form, TextField, PasswordField, DateField, IntegerField, BooleanField, RadioField, SelectField, TextAreaField

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

class crear_mod_TI(Form):
    id_TI = IntegerField('id_TI')
    codigo = TextField('codigo')
    nombre_TI = TextField('nombre_TI', validators = [Required()])
    descripcion = TextField('descripcion')
    
class crear_mod_atributoTI(Form):
    id = IntegerField('id')
    nombre = TextField('nombre', validators = [Required()])
    tipo = SelectField('tipo', choices = [('INT', 'Integer'), ('CHAR','Caracter'), 
                                          ('DATE', 'Fecha')],validators = [Required()])
    valorDefault = TextField('valorDefault', validators = [Required()])
    
class crear_mod_item(Form):
    id = IntegerField('id')
    descripcion = TextAreaField('descripcion')
    numero = IntegerField('numero')
    numero_TI = IntegerField('numero_TI')
    version = IntegerField('version')
    complejidad = IntegerField('complejidad')
    prioridad = SelectField('prioridad', choices = [(1,'Alta'), (2,'Media'), (3,'Baja')])
    estado = SelectField('estado', choices = [(1,'Aprobado'),(2,'Desaprobado'),
                                               (3,'Bloqueado'),(4,'Revision-Bloq'),
                                               (5,'Revision-Desbloq')])
    observaciones = TextAreaField('observaciones')

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

class comite_CrearForm(Form):
    nomComite = TextField('nomComite', validators = [Required()])
    u1 = RadioField()

