'''
Created on 20/04/2013

@author: cristian
'''
import os
import unittest
from app import db
from app.modelo import User2
#basedir = os.path.abspath(os.path.dirname(__file__))
class UsuarioTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, microblog.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = microblog.app.test_client()
        microblog.init_db()
    
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.DATABASE)

    def login(self, nombre, password):
        print 'fer2'
        return self.app.post('/login', data=dict(
                                                name = nombre,
                                                passWord = password),
                             follows_redirects = True
                             )
        
    def test_login(self):
        rv = self.login('admin', 'default')
        print str(rv.data)
    #def testSave(self):
    #   r = self.usuario1.add_usr()
    #    print "Creamos un usuario nuevo" + self.usuario1.nombre
    #    assertEqual(r, "Exito" )  
    #    self.contador = 1
    if __name__ == '__main__':
        unittest.main()