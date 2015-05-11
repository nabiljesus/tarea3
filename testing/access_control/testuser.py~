'''
Created on 10/05/2015
 
@author: Roberto Rinaldi y Nabil Marquez
'''

import unittest
from business.access_control.user import *
from business.access_control.dpt import *
from business.access_control.role import *

class loginTester(unittest.TestCase):
     
    def setUp(self):
        self.u = clsDBUser()
        self.r = clsRole()
        self.d = clsDpt()
#casos regulares
    def testDBUser(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')  
        self.u.insertar("juanjito", "juanjuan", "juAn123.4.5.6.7", "juan@juan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def testDBUser2(self):
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')   
        self.u.insertar("juanjito", "0", "juAn123.4.5.6.7", "juan@juan.com", 2, 3) 
        st=self.u.buscar("0")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"0")
        self.u.eliminar("0")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
#casos fronteras


    def testDBUser50n(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("AuS2CaV9lq8GbkJi174Af6hYDJ49ywbcx0Mf3rziTS9cJVfOja", "juanjuan", "juAn123.4.5.6.7", "juan@juan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def testDBUser16u(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "juanjuanjuanjuan", "juAn123.4.5.6.7", "juan@juan.com", 2, 3) 
        st=self.u.buscar("juanjuanjuanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuanjuanjuan")
        self.u.eliminar("juanjuanjuanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def testDBUser30c(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "juanjuan", "juAn123.4.5.6.7", "juanjuan@juanjuanjuanjuaan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
   
    def testDBUserpasinv1(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "juanjuan", "J.4jgjjj", "juan@juan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def testDBUserbothsame(self):  
        self.r.insertar(1,'prueba')
        self.d.insertar(1,'prueba')
        self.u.insertar("juanjito", "juanjuan", "J.4jgjjj", "juan@juan.com", 1, 1) 
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(1)
        self.d.eliminar(1)
        
    def testDBUseronezer(self):  
        self.r.insertar(0,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "juanjuan", "juAn123.4.5.6.7", "juan@juan.com", 2, 0)
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(0)
        self.d.eliminar(2)

    def testDBUserEmptyField(self):  
        self.r.insertar(0,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "", "juAn123.4.5.6.7", "juan@juan.com", 2, 0)
        st=self.u.buscar("")
        self.assertEqual(st,"")
        self.r.eliminar(0)
        self.d.eliminar(2)
#casos Esquinas

    def testDBUserTWoEmptyField(self):  
        self.r.insertar(0,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "", "", "juan@juan.com", 2, 0)
        st=self.u.buscar("")
        self.assertEqual(st,"")
        self.r.eliminar(0)
        self.d.eliminar(2)
        
    def testDBUserEmptyand16u(self):  
        self.r.insertar(1,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("", "juanjuanjuanjuan", "juAn123.4.5.6.7", "", 2, 1)
        st=self.u.buscar("")
        self.assertEqual(st,"")
        self.r.eliminar(1)
        self.d.eliminar(2)
        
    def testDBUserEmptyandzero(self):  
        self.r.insertar(0,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("", "juanjuAN", "juAn123.4.5.6.7", "", 2, 0)
        st=self.u.buscar("")
        self.assertEqual(st,"")
        self.r.eliminar(0)
        self.d.eliminar(2)
        
    def testDBUser30c50n(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("AuS2CaV9lq8GbkJi174Af6hYDJ49ywbcx0Mf3rziTS9cJVfOja", "juanjuan", "juAn123.4.5.6.7", "juanjuan@juanjuanjuanjuaan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        st=st.split()
        print(st)
        self.assertEqual(st[0],"juanjuan")
        self.u.eliminar("juanjuan")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
#casos maliciosos

    def testDBUserpasinv2(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("juanjito", "juanjuan", "jJ.4 jgjjj", "juan@juan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        self.assertEqual(st,"")
        self.r.eliminar(3)
        self.d.eliminar(2)
        
    def testDBUserpasinvRolDpt(self):  
        self.u.insertar("juanjito", "juanjuan", "jJ.4jgjjj", "juan@juan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        self.assertEqual(st,"")
        
    def testDBUserALLEmptyFieldAndZero(self):  
        self.r.insertar(0,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("", "", "", "", 0, 0)
        st=self.u.buscar("")
        self.assertEqual(st,"")
        self.r.eliminar(0)
        self.d.eliminar(2)
        
    def testDBUser30c51n(self):  
        self.r.insertar(3,'prueba')
        self.d.insertar(2,'prueba')
        self.u.insertar("AuS2CaV9lq8GbkJi174Adf6hYDJ49ywbcx0Mf3rziTS9cJVfOja", "juanjuan", "juAn123.4.5.6.7", "juanjuan@juanjuanjuanjuaan.com", 2, 3) 
        st=self.u.buscar("juanjuan")
        print(st)
        self.assertEqual(st,"")
        self.r.eliminar(3)
        self.d.eliminar(2)

    if __name__ == "__main__":
        unittest.main()