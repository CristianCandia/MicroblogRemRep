'''
Created on 01/05/2013

@author: cristian
'''
from app.modelo import User2
class ControllerUsr():
    def regUsuario(self, **kwargsUsr):
        usr = User2()
        for k, v in kwargsUsr.iteritems():
            if k == 'name':
                usr.name = v
            if k == 'passWord':
                usr.passWord = v
            if k == 'nombre':
                usr.nombre = v
            if k == 'apellido':
                usr.apellido = v
            if k == 'telefono':
                usr.telefono = v
            if k == 'ci':
                usr.ci = v
            if k == 'e_mail':
                usr.e_mail = v
        return usr.add_usr()