'''
Created on May 8, 2015

@author: Nabil J. Marquez
@author: Roberto Rinaldi
'''

import business.access_control.user, business.access_control.encrypt
from werkzeug import check_password_hash

class clsLogin():
    
    def encriptar(self, value):
        encri=business.access_control.encrypt.clsAccessControl()
        return encri.encript(value)

    def longitud(self, user_password):
        longi=business.access_control.encrypt.clsAccessControl()
        return longi.length_password(user_password)
    
    def check_password(self, username, trypass):
        decri=business.access_control.encrypt.clsAccessControl()
        usr=business.access_control.user.clsDBUser()
        passw=usr.buscar(username).split() #Obteniendo el hash de la db
        if passw!=[]:
            passw=passw[1]
            return decri.check_password(passw,trypass)
        else:
            return False
def main():
    logi=clsLogin()
    print(logi.encriptar("hola"))
    print(logi.encriptar("holaVAL3kas!?"))
    print(logi.longitud("hola"))
    print(logi.check_password("juanjuan2","baked"))
    print(logi.check_password("juanjuan2","!uAn123456789101"))
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()