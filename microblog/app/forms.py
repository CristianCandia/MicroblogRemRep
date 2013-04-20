'''
Created on 14/04/2013

@author: cristian
'''
from flask.ext.wtf import Form, TextField, PasswordField
from flask.ext.wtf import Required

class LoginForm(Form):
    nomUsr = TextField('openid', validators = [Required()])
    passWord = PasswordField('password', validators = [Required()])
    