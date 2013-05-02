'''
Created on 01/05/2013

@author: cristian
'''
from app.modelo import User2
class ControllerUsr():
    def regUsuario(self, **kwargsUsr):
        usr = User2()
        for k, v in kwargsUsr.iteritems():
            if k == 'nombre':
                usr.name = v
            if k == 'passWord':
                usr.passWord = v
            if k == 'role':
                usr.role = v
        return usr.add_usr()