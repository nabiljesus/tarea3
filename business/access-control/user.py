'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import os, sys
sys.path.append('../../data')
from model import *
from encrypt import *
from dpt import *
from role import *

DBSession = sessionmaker(bind = engine)

session = DBSession()

engine = create_engine(URL(**settings.DATABASE))

class clsDBUser():
       
    ''' Metodo insertar
        Inserta un nuevo usuario a la base de datos
    ''' 
        
    def insertar(self, fullname, username, password, email, iddpt, idrole):
       cript=clsAccessControl()
       dp=clsDpt()
       rl=clsRole()
       if self.buscar(username)=="" and rl.buscar(idrole)!="" and dp.buscar(iddpt)!="":
           passToUse=cript.encript(password)
           if passToUse!="":
               newuser = dbuser(fullname, username, passToUse, email, iddpt, idrole) 
               session.add(newuser)
               session.commit()
               return True
           else:
               return False
           return True
       else:
           return False
       
    ''' Metodo buscar
        Busca a traves del nombre un usuario dentro de la base de datos
    ''' 
        
    def buscar(self, iusername):
        result = engine.execute("select * from dbuser where username=\'"+iusername+"\';")
        out=""
        for u in session.query(dbuser).instances(result):
            out +='\n'+u.username+" "+u.password+" "+u.fullname+\
            " "+u.email+" "+str(u.iddpt)+" "+str(u.idrole)
        return out
        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un usuario
    ''' 
            
    def eliminar(self, iusername):
                
        session.query(dbuser).filter(dbuser.username == iusername).delete()
        session.commit()
        
    ''' Metodo listar
        Enlista todos los usarios con su informacion (no password).
    '''
        
    def listar(self):
        
        result = engine.execute("select * from dbuser")
        for u in session.query(dbuser).instances(result):
            print(u.username, u.fullname, u.email, u.iddpt, u.idrole)

      
    ''' Metodo modificar
        Modifica algun atributo de un usuario dentro de la base de datos
    ''' 
        
    def modificar(self, iusername, ifullname = None, ipassword = None, iemail = None, iidpt = None, iidrole = None):
        if self.buscar(iusername)!="":
            if ifullname != None:
                session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'fullname' : (ifullname) })
                session.commit()
            if ipassword != None:
                session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'password' : (ipassword) })
                session.commit()
            if iemail != None:
                session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'email' : (iemail) })
                session.commit()
            if iidpt != None:
                session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'idpt' : (iidpt) })
                session.commit()
            if iidrole != None:
                session.query(dbuser).filter(dbuser.username == iusername).\
                    update({'idrole' : (iidrole) }) 
                session.commit()
            
def main():
    usr = clsDBUser()
    usr.insertar("juanjito", "juanjuan", "juAn123.4.5.6.7", "juan@juan.com", 2, 3) 
    usr.insertar("juanjito2", "juanjuan2", "!uAn123456789101", "juan2@juan.com", 3, 3) 
    usr.insertar("juanjito3", "juanjuan3", "juAn123.4.5.6.7.", "juan2@juan.com", 3, 3) 
    
    usr.eliminar("juanjuan")
    
    usr.modificar("juanjuan2","erjuan")
    usr.listar()
    print()
    print(usr.buscar("juanjuan2"))
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()

