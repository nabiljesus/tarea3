'''
Created on May 6, 2015

@author: Meggie y Cristina
'''

import os

import settings

from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy.engine.url import URL

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from sqlalchemy.orm import sessionmaker

db = declarative_base()

# Clase Usuario

class User(db):
    
    __tablename__ = 'Users'
    fullname = Column(String(50), unique = True)
    username = Column(String(16), primary_key = True)
    password = Column(String(16), unique = True)
    email = Column(String(30), unique = True)
    iddpt = Column(Integer, ForeignKey('Departaments.iddpt'))
    idrole = Column(Integer, ForeignKey('Roles.idrole'))
    
    ''' Metodo init
        Constructor del usuario
    ''' 
    
    def __init__(self, fullname, username, password, email, iddpt, idrole):
        
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.iddpt = iddpt 
        self.idrole = idrole

# Clase Departamento

class Dpt(db):
    
    __tablename__ = 'Departaments'
    iddpt = Column(Integer, primary_key = True)
    namedpt = Column(String(50), unique = True)
    users = relationship('User', backref='Departaments')
    
    ''' Metodo init
        Constructor del departamento
    ''' 
    
    def __init__(self, iddpt, namedpt):
        
        self.iddpt = iddpt
        self.namedpt = namedpt

# Clase Role

class Role(db):
    
    __tablename__ = 'Roles'
    idrole = Column(Integer, primary_key = True)
    namerole = Column(String(50), unique = True)
    users = relationship('User', backref='Roles')
    
    ''' Metodo init
        Constructor del rol
    ''' 
    
    def __init__(self, idrole, namerole = None):
        
        self.idrole = idrole 
        self.namerole = namerole
     

engine = create_engine(URL(**settings.DATABASE))

db.metadata.drop_all(engine)
db.metadata.create_all(engine)
