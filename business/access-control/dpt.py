'''
Created on May 6, 2015

@author: Meggie y Cristina
'''
from model import *

DBSession = sessionmaker(bind = engine)

session = DBSession()

engine = create_engine(URL(**settings.DATABASE))

class clsDpt():
        
    ''' Metodo insertar
        Inserta un nuevo departamento a la base de datos
    '''  
          
    def insertar(self, iddpt, namedpt):
        if self.buscar(iddpt)=="":
            newdpt = dpt(iddpt, namedpt) 
            session.add(newdpt)
            session.commit()
            return True
        else:
            return False
        
    ''' Metodo buscar
        Busca a traves del nombre un departamento dentro de la base de datos
    '''    
        
    def buscar(self, iiddpt):
        out=""
        result = engine.execute("select * from dpt where iddpt="+str(iiddpt)+";")
        for u in session.query(dpt).instances(result):
            out+='\n'+str(u.iddpt)+" "+u.namedpt
        return out

        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un departamento
    '''   
     
    def eliminar(self, iidpt):
        
        session.query(dbuser).filter(dbuser.iddpt == iidpt).delete()
        session.commit()
        
        session.query(dpt).filter(dpt.iddpt == iidpt).delete(synchronize_session=False)
        session.commit()
    
    ''' Metodo listar
        Lista todas las columnas en departamento.
    '''   
     
    def listar(self):
        
        result = engine.execute("select * from dpt")
        for u in session.query(dpt).instances(result):
            print(u.iddpt,u.namedpt)
        
    ''' Metodo modificar
        Modifica algun atributo de un departamento dentro de la base de datos
    '''  
          
    def modificar(self, iidpt, inamedpt):
        
        if self.buscar(iidpt)!="":
                
            session.query(dpt).filter(dpt.iddpt == iidpt).\
                 update({'namedpt' : (inamedpt) })
            session.commit()


def main():
    dpts = clsDpt()
    dpts.insertar(1, 'dpt1') 
    dpts.insertar(2, 'dpt2')
    dpts.insertar(3, 'dpt3') 
    
    dpts.eliminar(1)
    
    dpts.modificar(2, 'dpt222')
    print()
    print(dpts.buscar(2))
    print()
    dpts.listar()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()      

        
       