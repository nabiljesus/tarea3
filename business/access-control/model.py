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

DB = declarative_base()

class dbuser(DB):
    
    __tablename__ = 'dbuser'
    fullname = Column(String(50))
    username = Column(String(16), primary_key = True)
    password = Column(String(16))
    email = Column(String(30))
    iddpt = Column(Integer, ForeignKey('dpt.iddpt'))
    idrole = Column(Integer, ForeignKey('role.idrole'))
    
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

class dpt(DB):
    
    __tablename__ = 'dpt'
    iddpt = Column(Integer, primary_key = True)
    namedpt = Column(String(50), unique = True)
    users = relationship('dbuser', backref='dpt')
    
    ''' Metodo init
        Constructor del departamento
    ''' 
    
    def __init__(self, iddpt, namedpt):
        
        self.iddpt = iddpt
        self.namedpt = namedpt

class role(DB):
    
    __tablename__ = 'role'
    idrole = Column(Integer, primary_key = True)
    namerole = Column(String(50), unique = True)
    users = relationship('dbuser', backref='role')
    
    ''' Metodo init
        Constructor del rol
    ''' 
    
    def __init__(self, idrole, namerole = None):
        
        self.idrole = idrole 
        self.namerole = namerole
     

engine = create_engine(URL(**settings.DATABASE))

DB.metadata.drop_all(engine)
DB.metadata.create_all(engine)
