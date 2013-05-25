'''
Created on 05/05/2013

@author: cristian
'''

import unittest
import os

from app import db
from app.modelo import User2, Proyecto
from app.controlador import ControllerUsr
from app.controlador.contProy import ControllerProy

basedir = os.path.abspath(os.path.dirname(__file__))

class TestUser2(unittest.TestCase):
    def setUp(self):
        self.user1 = User2(name="name", passWord="name", nombre="cristian",
                           apellido="candia", telefono="123-321",
                           ci = "4673", e_mail= "otro@email.com")
        self.proy1 = Proyecto(nombre = 'proyecto_test',
                              descripcion = 'Proyecto de test',
                              fecha_de_creacion = '2013-05-05',
                              complejidad_total = 3,
                              estado = 'En espera')
        self.bandera = 0
        self.bandera1 = 0
        self.c_usr = ControllerUsr()
        self.c_proy = ControllerProy()
    
    def testGuardar(self):
        resp = self.user1.add_usr()
        print "Creamos un usuario nuevo: " + self.user1.nombre
        self.assertEqual(resp, "Exito" )
        self.bandera = 1
        
    def testModificarUsuario(self):
        user2 = self.c_usr.getUsrName(name = 'admin')
        print str(user2.nombre)
        user2.nombre = "CRISTIAN_MIGUEL"
        user2.apellido = 'CANDIA_DELGADO'
        resp = self.c_usr.modUsuario(user2)
        self.assertEqual(resp, 'Exito')
        
    def testCrearProyecto(self):
        resp = self.proy1.add_proy()
        print "Creamos un proyecto nuevo: " + self.proy1.nombre
        self.assertEqual(resp, "Exito" )
        self.bandera1 = 1
    
    def testModificarProyecto(self):
        proy2 = self.c_proy.getProyNombre(nombre = 'is 2')
        proy2.descripcion = 'descripcion2'
        resp = self.c_proy.modProyecto(proy2)
        self.assertEqual(resp, 'Exito')

    def tearDown(self):
        if self.bandera == 1:
            self.user1.delete_usr()
        if self.bandera1 == 1:
            self.proy1.delete_proyecto()
        user2 = self.c_usr.getUsrName(name = 'admin')
        user2.nombre = "CRISTIAN"
        user2.apellido = 'CANDIA'
        resp = self.c_usr.modUsuario(user2)
        proy2 = self.c_proy.getProyNombre(nombre = 'is 2')
        proy2.descripcion = 'proyecto is2'
        resp = self.c_proy.modProyecto(proy2)

if __name__ == '__main__':
        unittest.main()
    