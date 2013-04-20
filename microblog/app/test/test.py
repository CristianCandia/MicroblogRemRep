'''
Created on 20/04/2013

@author: cristian
'''
import os
import microblog
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, microblog.app.config['DATABASE'] = tempfile.mkstemp()
        microblog.app.config['TESTING'] = True
        self.app = microblog.app.test_client()
        microblog.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(microblog.app.config['DATABASE'])
        
    def crear_usuario(self, username, passWord):
        return self.app.post('/usr_crear', data=dict(
        username=username,
        passWord=passWord
    ), follow_redirects=True)
        
    def test_crear_usuario(self):
        import json
        assert json.loads(self.crear_usuario('admin', 'admin')) == True

if __name__ == '__main__':
    unittest.main()
