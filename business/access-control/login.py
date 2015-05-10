'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import model
import user
import encrypt

class clsLogin():
    
    def encriptar(self, value):
        encri=encrypt.clsAccessControl()
        return encri.encript(value)

    def longitud(self, user_password):
        longi=encrypt.clsAccessControl()
        return encri.length_password(user_password)
    
    def check_password(self, username, trypass):
        longi=encrypt.clsAccessControl()
        usr=user.clsDBUser()
        passw=usr.buscar(username)[1] #Obteniendo el hash de la db
        return encri.check_password(passw,trypass)