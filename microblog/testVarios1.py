'''
Created on 05/05/2013

@author: cristian
'''

import unittest
import os

from app import db
from app.modelo import User2
from app.controlador import ControllerUsr

basedir = os.path.abspath(os.path.dirname(__file__))

class TestUser2(unittest.TestCase):
    def setUp(self):
        self.user1 = User2(name="name", passWord="name", nombre="cristian",
                           apellido="candia", telefono="123-321",
                           ci = "4673", e_mail= "@email.com")
        self.user2 = User2.query.filter_by(name = 'admin').first()
        self.bandera = 0
        self.c_usr = ControllerUsr()
    
    def testGuardar(self):
        resp = self.user1.add_usr()
        print "Creamos un usuario nuevo: " + self.user1.nombre
        self.assertEqual(resp, "Exito" )
        self.bandera = 1
        
    def testImprimePermisos(self):
        permisos = self.c_usr.getPermisos(self.user2)
        if permisos is None:
            print 'no trajo nada'
        for p in permisos:
            print p.nombre
        print 'hizo algo'       
        
    def tearDown(self):
        if self.bandera == 1:
            self.user1.delete_usr()

if __name__ == '__main__':
        unittest.main()
    