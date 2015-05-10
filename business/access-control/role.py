'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import sys
import os

import model

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind = model.engine)

session = DBSession()

class clsRole():
          
    ''' Metodo insertar
        Inserta un nuevo rol a la base de datos
    ''' 
        
    def insertar(self, idrole, namerole):
        
        role = model.role(idrole, namerole) 
        session.add(role)
        session.commit()
        
    ''' Metodo buscar
        Busca a traves del nombre un rol dentro de la base de datos
    ''' 
        
    def buscar(self, role):
        
        busq = session.query(model.role).filter(model.role.idrole == role).all()
        return busq
        
    ''' Metodo eliminar
        Elimina dentro de la base de datos a un rol
    ''' 
    
    def eliminar(self, role):
        
        query = self.buscar(role)
        
        session.query(model.role).filter(model.role.idrole == role).delete()
        session.commit()
        
    ''' Metodo modificar
        Modifica algun atributo de un rol dentro de la base de datos
    ''' 
        
    def modificar(self, role, iname):
        
        query = self.buscar(role)
                
        session.query(model.role).filter(model.role.idrole == role).\
             update({'namerole' : (iname) })
        session.commit()
    
        
roles = clsRole()
roles.insertar(1, 'role') 
roles.insertar(2, 'role2')
roles.insertar(3, 'role3') 

roles.eliminar(1)

roles.modificar(2, 'rol222')
