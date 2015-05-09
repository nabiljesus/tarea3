'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import model
import role
import dpt

class clsUser():
       
    ''' Metodo insertar
        Inserta un nuevo usuario a la base de datos
    ''' 
        
    def insertar(self, fullname, username, password, email, iddpt, idrole):
        
       user = model.User(fullname, username, password, email, iddpt, idrole) 
       session.add(user)
       session.commit()
       
    ''' Metodo buscar
        Busca a traves del nombre un usuario dentro de la base de datos
    ''' 
        
    def buscar(self, iusername):
        
        busq = session.query(model.User).filter(model.User.username == iusername).all()
        return busq
        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un usuario
    ''' 
    
    def eliminar(self, iusername):
        
        username = model.User(username = iusername)
        session.delete(username)
        session.commit()
        
    ''' Metodo modificar
        Modifica algun atributo de un usuario dentro de la base de datos
    ''' 
        
    def modificar(self, iusername, ifullname = None, ipassword = None, iemail = None, iidpt = None, iidrole = None):
        
        user = model.Role.buscar(iusername)
        
        if ifullname != None:
            user.fullname = ifullname
        if ipassword != None:
            user.password = ipassword
        if iemail != None:
            user.email = iemail
        if iidpt != None:
            user.idpt = iidpt
        if iidrole != None:
            user.idrole = iidrole 
        
        session.add(user)
        session.commit()
        
