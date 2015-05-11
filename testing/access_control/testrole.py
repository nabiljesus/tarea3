'''
Created on 10/05/2015
 
@author: Roberto Rinaldi y Nabil Marquez
'''
import unittest
from business.access_control.role import *
 
class roleTester(unittest.TestCase):
     
    def setUp(self):
        self.d = role()
    
    
    def testrole(self):  
        self.d.insertar(10,'nombre')
        st=self.d.buscar(10)
        st.split()
        self.assertEqual(True,st[0],10)
    
    def testrole2(self):  
        self.d.insertar(0,'nombre1')
        st=self.d.buscar(0)
        st.split()
        self.assertEqual(True,st[0],0)
        
    def testdrolevacio(self):  
        self.d.insertar(11,'')
        st=self.d.buscar(11)
        self.assertEqual(True,st,'')
   
    def testrole3(self):  
        self.d.insertar(13,'n')
        st=self.d.buscar(13)
        st.split()
        self.assertEqual(True,st[0],13)
    
    def testrole50(self):  
        self.d.insertar(14,'nombrenombrenombrenombrenombrenombrenombrenombrenombrenombre')
        st=self.d.buscar(14)
        self.assertEqual(True,st,'')
     
    def testrole51(self):  
        self.d.insertar(15,'nombrenombrenombrenombrenombrenombrenombrenombrenombrenombren')
        st=self.d.buscar(15)
        st.split()
        self.assertEqual(True,st[0],15)
        
    def testrole4(self):  
        self.d.insertar(16,'nombre@#')
        st=self.d.buscar(16)
        st.split()
        self.assertEqual(True,st[0],16)
    
    def testrole5(self):  
        self.d.insertar(17,'nombre1111')
        st=self.d.buscar(17)
        st.split()
        self.assertEqual(True,st[0],17)
        
    def testrole6(self):  
        self.d.insertar(18,'1234')
        st=self.d.buscar(18)
        st.split()
        self.assertEqual(True,st[0],18)
        
    def testrole7(self):  
        self.d.insertar(19,'1')
        st=self.d.buscar(19)
        st.split()
        self.assertEqual(True,st[0],19)
    
    def testrole8(self):  
        self.d.insertar(20,'%')
        st=self.d.buscar(20)
        st.split()
        self.assertEqual(True,st[0],20)
    
    def testrole9(self):  
        self.d.insertar(21,'nombre nombre')
        st=self.d.buscar(21)
        st.split()
        self.assertEqual(True,st[0],21)
        
        
        
        
        
    def testdrole9(self):  
        self.d.eliminar(10)
        st=self.d.buscar(10)
        self.assertEqual(True,st,'')
        
        
    def testrole9(self):  
        self.d.modificar(13,'nuevonombre')
        st=self.d.buscar(13)
        st.split()
        self.assertEqual(True,st[1],'nuevonombre')
        
    
    
         
         
    
   
     
         
    if __name__ == "__main__":
        unittest.main()