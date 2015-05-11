'''
Created on May 7, 2015

@author: root
'''
'''
Created on May 6, 2015

@author: root
'''

import os

from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import *

from sqlalchemy.engine.url import URL

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

db = declarative_base()
#db = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(db,'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(db, 'db_repository')

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] =\
#'postgresql://11-10104:cebm5594@usul.ldc.usb.ve/Software3'
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#db = SQLAlchemy(app)

# Clase Usuario
class User(db):
    
    __tablename__ = 'Users'
    fullname = Column(String(50), unique = True)
    username = Column(String(16), primary_key = True)
    password = Column(String(16), unique = True)
    email = Column(String(30), unique = True)
    iddpt = Column(Integer, ForeignKey('Departaments.iddpt'))
    idrole = Column(Integer, ForeignKey('Roles.idrole'))

# Clase Departamento
class Dpt(db):
    
    __tablename__ = 'Departaments'
    iddpt = Column(Integer, primary_key = True)
    namedpt = Column(String(50), unique = True)
    users = relationship('User', backref='Departaments')

# Clase Role
class Role(db):
    
    __tablename__ = 'Roles'
    idrole = Column(Integer, primary_key = True)
    namerole = Column(String(50), unique = True)
    users = relationship('User', backref='Roles')

'''
# Clase para la tabla de Logins
class Login(db.Model):
    
    __tablename__='Login' 
    username = db.Column(db.String(16), db.ForeignKey('User.username'))
    password = db.Column(db.String(16), db.ForeignKey('User.password'))
    
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        ohast = ''
 '''
        

#engine = create_engine(URL(**settings.DATABASE))

db.drop_all()
db.create_all()
