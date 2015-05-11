'''
Created on 10/05/2015
 
@author: Roberto Rinaldi y Nabil Marquez
'''
import unittest
from business.access_control.role import *
 
class roleTester(unittest.TestCase):
     
    def setUp(self):
        self.d = clsRole()
    
    # caso valido 
    def testrole(self):  
        self.d.insertar(10,'nombre')
        st=self.d.buscar(10)
        st=st.split()
        self.assertEqual(int(st[0]),10)
    #casos frontera
    def testrole2(self):  
        self.d.insertar(0,'nombre1')
        st=self.d.buscar(0)
        st=st.split()
        self.assertEqual(int(st[0]),0)

   
    def testrole3(self):  
        self.d.insertar(13,'n')
        st=self.d.buscar(13)
        st=st.split()
        self.assertEqual(int(st[0]),13)
    
    def testrole50(self):  
        self.d.insertar(14,'nombrenombrenombrenombrenombrenombrenombrenombrenombrenombre')
        st=self.d.buscar(14)
        self.assertEqual(st,'')
     
    def testrole51(self):  
        self.d.insertar(15,'nombrenombrenombrenombrenombrenombrenombrenombrenombrenombren')
        st=self.d.buscar(15)
        self.assertEqual(st,'')
        
    def testrole4(self):  
        self.d.insertar(16,'nombre@#')
        st=self.d.buscar(16)
        st=st.split()
        self.assertEqual(int(st[0]),16)
    
    def testrole5(self):  
        self.d.insertar(17,'nombre1111')
        st=self.d.buscar(17)
        st=st.split()
        self.assertEqual(int(st[0]),17)
        
    def testrole6(self):  
        self.d.insertar(18,'1234')
        st=self.d.buscar(18)
        st=st.split()
        self.assertEqual(int(st[0]),18)
        
    def testrole7(self):  
        self.d.insertar(19,'1')
        st=self.d.buscar(19)
        st=st.split()
        self.assertEqual(int(st[0]),19)
    
    def testrole8(self):  
        self.d.insertar(20,'%')
        st=self.d.buscar(20)
        st=st.split()
        self.assertEqual(int(st[0]),20)
    
    def testrole9(self):  
        self.d.insertar(21,'nombre nombre')
        st=self.d.buscar(21)
        st=st.split()
        self.assertEqual(int(st[0]),21)


     # esquina malicia
        
    def testdrolevacio(self):  
        self.d.insertar(11,'')
        st=self.d.buscar(11)
        self.assertEqual(st,'')
        
        
        
        
    # caso eliminar 
    def testdrole9(self):  
        self.d.eliminar(10)
        st=self.d.buscar(10)
        self.assertEqual(st,'')
      
      # caso modificar  
        
    def testrole9(self):  
        self.d.modificar(13,'nuevonombre')
        st=self.d.buscar(13)
        st=st.split()
        self.assertEqual(st[1],'nuevonombre')
        
    
    
         
         
    
   
     
         
    if __name__ == "__main__":
        unittest.main()