'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import model

class clsDpt():
        
    ''' Metodo insertar
        Inserta un nuevo departamento a la base de datos
    '''  
          
    def insertar(self, iddpt, namedpt):
        
        dpt = model.Dpt(iddpt, namedpt) 
        session.add(dpt)
        session.commit()
        
    ''' Metodo buscar
        Busca a traves del nombre un departamento dentro de la base de datos
    '''    
        
    def buscar(self, dpt):
        
        busq = session.query(model.Dpt).filter(model.Dpt.iddpt == dpt).all()
        return busq
        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un departamento
    '''   
     
    def eliminar(self, dpt):
        
        query = self.buscar(dpt)
        
        session.query(model.Dpt).filter(model.Role.iddpt == dpt).delete()
        session.commit()
        
    ''' Metodo modificar
        Modifica algun atributo de un departamento dentro de la base de datos
    '''  
          
    def modificar(self, iidpt, inamedpt):
        
        query = self.buscar(iidpt)
                
        session.query(model.Role).filter(model.Role.iddpt == iidpt).\
             update({'namedpt' : (inamedpt) })
        session.commit()
        
dpts = clsDpt()
dpts.insertar(1, 'dpt1') 
dpts.insertar(2, 'dpt2')
dpts.insertar(3, 'dpt3') 

dpts.eliminar(1)

dpts.modificar(2, 'dpt222')
        
       