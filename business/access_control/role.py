'''
Created on May 8, 2015

@author: Nabil J. Marquez
@author: Roberto Rinaldi
'''

from data.model import *

DBSession = sessionmaker(bind = engine)

session = DBSession()

engine = create_engine(URL(**data.settings.DATABASE))

class clsRole():
          
    ''' Metodo insertar
        Inserta un nuevo rol a la base de datos
    ''' 
        
    def insertar(self, idrole, namerole):
        verif=self.buscar(idrole)=="" and idrole>=0 and 0<len(namerole)<=50
        if verif:
            newrole = role(idrole, namerole) 
            session.add(newrole)
            session.commit()
            return True
        else:
            return False
        
    ''' Metodo buscar
        Busca a traves del nombre un rol dentro de la base de datos y lo imprime
    ''' 
        
    def buscar(self, irole):
        out=""
        result = engine.execute("select * from role where idrole="+str(irole)+";")
        if result!="":
            for u in session.query(role).instances(result):
                out+=str(u.idrole)+" "+u.namerole+'\n'
        return out

        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un rol
    ''' 
    
    def eliminar(self, irole):
        
        '''Eliminacion en cascada'''
        
        session.query(dbuser).filter(dbuser.idrole == irole).delete()
        session.commit()
        
        session.query(role).filter(role.idrole == irole).delete()
        session.commit()
 
    ''' Metodo listar
        Lista todas las columnas en role.
    '''   
     
    def listar(self):
        
        result = engine.execute("select * from role")
        for u in session.query(role).instances(result):
            print(u.idrole,u.namerole)
        
    ''' Metodo modificar
        Modifica algun atributo de un rol dentro de la base de datos
    ''' 

    def modificar(self, irole, iname):
                
        session.query(role).filter(role.idrole == irole).\
             update({'namerole' : (iname) })
        session.commit()
    

def main():
    roles = clsRole()
    roles.insertar(1, 'role') 
    roles.insertar(2, 'role2')
    roles.insertar(3, 'role3') 
    
    roles.eliminar(1)
    
    roles.modificar(2, 'rol222')
    print("sesco")
    roles.listar()
    print("sesco")
    print(roles.buscar(2))
    print("sesco")

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
        

