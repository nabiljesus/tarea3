'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import model
import role
import dpt

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind = model.engine)

session = DBSession()

class clsDBUser():
       
    ''' Metodo insertar
        Inserta un nuevo usuario a la base de datos
    ''' 
        
    def insertar(self, fullname, username, password, email, iddpt, idrole):
        
       user = model.dbuser(fullname, username, password, email, iddpt, idrole) 
       session.add(user)
       session.commit()
       
    ''' Metodo buscar
        Busca a traves del nombre un usuario dentro de la base de datos
    ''' 
        
    def buscar(self, iusername):
        
        busq = session.query(model.dbuser).filter(model.dbuser.username == iusername).all()
        return busq
        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un usuario
    ''' 
    
    def eliminar(self, iusername):
        query = self.buscar(iusername)
        
        session.query(model.dbuser).filter(model.dbuser.username == iusername).delete()
        session.commit()
        
    ''' Metodo modificar
        Modifica algun atributo de un usuario dentro de la base de datos
    ''' 
        
    def modificar(self, iusername, ifullname = None, ipassword = None, iemail = None, iidpt = None, iidrole = None):
        
        user = self.buscar(iusername)


        if ifullname != None:
            session.query(model.dbuser).filter(model.dbuser.username == iusername).\
                update({'fullname' : (ifullname) })
            session.commit()
        if ipassword != None:
            session.query(model.dbuser).filter(model.dbuser.username == iusername).\
                update({'password' : (ipassword) })
            session.commit()
        if iemail != None:
            session.query(model.dbuser).filter(model.dbuser.username == iusername).\
                update({'email' : (iemail) })
            session.commit()
        if iidpt != None:
            session.query(model.dbuser).filter(model.dbuser.username == iusername).\
                update({'idpt' : (iidpt) })
            session.commit()
        if iidrole != None:
            session.query(model.dbuser).filter(model.dbuser.username == iusername).\
                update({'idrole' : (iidrole) }) 
            session.commit()

usr = clsDBUser()
usr.insertar("juanjito", "juanjuan", "juan123", "juan@juan.com", 2, 3) 
usr.insertar("juanjito2", "juanjuan2", "juan123", "juan2@juan.com", 3, 3) 
usr.insertar("juanjito3", "juanjuan3", "juan123", "juan2@juan.com", 3, 3) 

usr.eliminar("juanjuan")

usr.modificar("juanjuan2","erjuan")
