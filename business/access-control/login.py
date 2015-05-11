'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import user, encrypt
from werkzeug import check_password_hash

class clsLogin():
    
    def encriptar(self, value):
        encri=encrypt.clsAccessControl()
        return encri.encript(value)

    def longitud(self, user_password):
        longi=encrypt.clsAccessControl()
        return longi.length_password(user_password)
    
    def check_password(self, username, trypass):
        decri=encrypt.clsAccessControl()
        usr=user.clsDBUser()
        passw=usr.buscar(username).split() #Obteniendo el hash de la db
        if passw!=[]:
            print(passw)
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