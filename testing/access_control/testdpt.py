'''
Created on 10/05/2015
 
@author: Roberto Rinaldi y Nabil Marquez
'''
import unittest
from business.access_control.dpt import *
 
class dptTester(unittest.TestCase):
     
    def setUp(self):
        self.d = clsDpt()
    
    def testdpt(self):  
        self.d.insertar(10,'nombre')
        st=self.d.buscar(10)
        st=st.split()
        print(st)
        self.assertEqual(st[0],'10')
    
    def testdpt2(self):  
        self.d.insertar(0,'nombre1')
        st=self.d.buscar(0)
        st=st.split()
        self.assertEqual(st[0],'0')
        
    def testdptvacio(self):  
        self.d.insertar(11,'')
        st=self.d.buscar(11)
        self.assertEqual(st,'')
   
    def testdpt3(self):  
        self.d.insertar(13,'n')
        st=self.d.buscar(13)
        st=st.split()
        self.assertEqual(st[0],'13')
    
    def testdpt50(self):  
        self.d.insertar(14,'nombrenombrenombrenombrenombrenombrenombrenombreno')
        st=self.d.buscar(14)
        st=st.split()
        self.assertEqual(st[0],'14')
     
    def testdpt51(self):  
        self.d.insertar(15,'nombrenombrenombrenombrenombrenombrenombrenombrenomb')
        st=self.d.buscar(15)
        self.assertEqual(st,'')
        
    def testdpt4(self):  
        self.d.insertar(16,'nombre@#')
        st=self.d.buscar(16)
        st=st.split()
        self.assertEqual(st[0],'16')
    
    def testdpt5(self):  
        self.d.insertar(17,'nombre1111')
        st=self.d.buscar(17)
        st=st.split()
        self.assertEqual(st[0],'17')
        
    def testdpt6(self):  
        self.d.insertar(18,'1234')
        st=self.d.buscar(18)
        st=st.split()
        self.assertEqual(st[0],'18')
        
    def testdpt7(self):  
        self.d.insertar(19,'1')
        st=self.d.buscar(19)
        st=st.split()
        self.assertEqual(st[0],'19')
    
    def testdpt8(self):  
        self.d.insertar(20,'%')
        st=self.d.buscar(20)
        st=st.split()
        self.assertEqual(st[0],'20')
    
    def testdpt9(self):  
        self.d.insertar(21,'nombre nombre')
        st=self.d.buscar(21)
        st=st.split()
        self.assertEqual(st[0],'21')
        
        
    def testdpt9(self):  
        self.d.eliminar(10)
        st=self.d.buscar(10)
        self.assertEqual(True,st,'')
        
        
    def testdpt9(self):  
        self.d.modificar(13,'nuevonombre')
        st=self.d.buscar(13)
        st=st.split()
        self.assertEqual(st[1],'nuevonombre')
        
    
    
         
         
    
   
     
         
    if __name__ == "__main__":
        unittest.main()