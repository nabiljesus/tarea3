'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import model
import user

class clsLogin():

    def matchRegex(self, value, regularExpression):
        
        lc = re.compile(regularExpression)
        x= lc.findall(value)
        return x!=[] 
    
    def encriptar(self, value):
        
        # Inicializacion
        oHash=""    
        # Verificar la longitud del password
        olength_password=self.length_password(value)
        if olength_password>=8 and olength_password<=16:
            #Vericar que tenga minuscula
            if (self.matchRegex(value,'[a-z]+')):
                #Vericar que tenga mayuscula
                if (self.matchRegex(value,'[A-Z]+')):
                    #Vericar que tenga numero
                    if (self.matchRegex(value,'[0-9]+')):
                        #Vericar que tenga caracter especial
                        if (self.matchRegex(value,'(\.|\#|\!|\@|\?|\¿|\¡|\+|\-|\_|\%|\*|\(|\))+')):
                            #Vericar que no tenga otros caracteres
                            lc = re.compile('(\.|\#|\!|\@|\?|\¿|\¡|\+|\-|\_|\%|\*|\(|\)|[0-9]|[A-Z]|[a-z])')
                            x= lc.findall(value)
                            y=any(e not in x  for e in value)
                            if (not y):
                                # uuid es usado para generar numeros random
                                salt = uuid.uuid4().hex
                                # hash
                                oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt    
                                return oHash
                            else:
                                print('El password contiene caracteres invalidos.')
                                return oHash
            print('El password carece de caracteres requeridos.')
        else:
            print('El Password no posee la cantidad de caracteres requerida')
        return oHash
      
    def check_password(self, oPassworkEncript, oCheckPassword):
        
            oPassworkEncript, salt = oPassworkEncript.split(':')
            return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
    
    def longitud(self, user_password):
        
        # uuid es usado para generar numeros random
        return len(user_password)
    