'''
Created on 05/05/2013

@author: cristian
'''

import unittest

class TestUser2(unittest.TestCase):  
        def setUp(self):
            self.contador = 0
            self.pru = 0
      
        def test_test1(self):  
            resp = 0
            print "Hacemos una prueba"
            self.assertEqual(resp, 0 )  
            self.pru = 1
        def test_test2(self):  
            resp = 0
            print "Hacemos una prueba"
            self.assertEqual(resp, 0 )  
            self.pru = 1
        def test_test3(self):  
            resp = 0
            print "Hacemos una prueba"
            self.assertEqual(resp, 0 )  
            self.pru = 1
        def test_test4(self):  
            resp = 0
            print "Hacemos una prueba"
            self.assertEqual(resp, 0 )  
            self.pru = 1
                
        def tearDown(self):  
            if self.pru == 1:
                print "hice una prueba"