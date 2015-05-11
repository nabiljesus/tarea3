'''
Created on 10/05/2015
 
@author: Roberto Rinaldi y Nabil Marquez
'''

import unittest
from business.access_control.user import *
from business.access_control.dpt import *
from business.access_control.role import *
from business.access_control.login import *


class loginTester(unittest.TestCase):
     
    def setUp(self):
        self.u = clsDBUser()
        self.r = clsRole()
        self.d = clsDpt()
        self.l = clsLogin()
        
    ''' Los metodos longitud y encriptar son una llamada a los ya correctamente probados metodos
    length_password y encript, por lo que su prueba es aceptada como correcta'''
        
#casos regulares
    def testLogin(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuan", "juAn123.4.5.6.7", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("juanjuan", "juAn123.4.5.6.7"))
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def testLogin2(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuajo", "dadaS5.!", "juan@juan.com", 2, 3) 
        self.assertFalse(self.l.check_password("juanjuajo", "juAn12345!"))
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)

#Casos Frontera

    def test1u(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "j", "dadaS5.!", "juan@juan.com", 2, 3) 
        self.assertFalse(self.l.check_password("j", "juAn12345!"))
        self.u.eliminar("j")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def test8p(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "jojoto", "!.aV5678", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("jojoto", "!.aV5678"))
        self.u.eliminar("jojoto")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def test16p(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "jojoto", "!.aV567891023456", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("jojoto", "!.aV567891023456"))
        self.u.eliminar("jojoto")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def test16u(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuanjuanjuan", "dadaS5.!", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("juanjuanjuanjuan", "dadaS5.!"))
        self.u.eliminar("juanjuanjuanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
#Casos esquina

    def test16p1u(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "j", "!.aV567891023456", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("j", "!.aV567891023456"))
        self.u.eliminar("j")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def test16p16u(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuanjuanjuan", "!.aV567891023456", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("juanjuanjuanjuan", "!.aV567891023456"))
        self.u.eliminar("juanjuanjuanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def test8p16u(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuanjuanjuan", "!.aV5678", "juan@juan.com", 2, 3) 
        self.assertTrue(self.l.check_password("juanjuanjuanjuan", "!.aV5678"))
        self.u.eliminar("juanjuanjuanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)

#Casos de malicia

    def testwuserpass(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuanjuanjuan", "!.aV5678", "juan@juan.com", 2, 3) 
        self.assertFalse(self.l.check_password("ddd", "asdasf asdgasdg sdf"))
        self.u.eliminar("juanjuanjuanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)

    def testEmpty(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuanjuanjuan", "!.aV5678", "juan@juan.com", 2, 3) 
        self.assertFalse(self.l.check_password("", ""))
        self.u.eliminar("juanjuanjuanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)

    def test17p17u(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juaanjuanjuanjuan", "!.aaV567891023456", "juan@juan.com", 2, 3) 
        self.assertFalse(self.l.check_password("juaanjuanjuanjuan", "!.aaV567891023456"))
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    if __name__ == "__main__":
        unittest.main()