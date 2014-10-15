import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    #table for all individual people that have accounts
    #typically we will see 1 VPN account per person
    id = Column(Integer, primary_key=True)
    fullName = Column(String(100), nullable=False)
    vpnUserName = Column(String(25), nullable=False)
    vpnPassword = Column(String(25), nullable=False)

class IPAddress(Base):
    __tablename__ = "IPAddress"
    id = Column(Integer, primary_key=True)
    IP = Column(String(16), nullable=False, unique=True)
    subnet = Column(String(12), nullable=False)

class VisitByUser(Base):
    __tablename__ = "VisitByUser"
    id = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)
    IPID = Column(Integer, ForeignKey('IPAddress.id'))
    IP = relationship(IPAddress)
    dateTime = Column(DateTime, nullable=False)

engine = create_engine('sqlite:///sqlalchemy_sqlite.db')

Base.metadata.create_all(engine)





















'''
class IPByUser(Base):
    __tablename__ = "IPByUser"
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('User.id'))
    IPId = Column(Integer, ForeignKey('IPAddress.id'))
    count = Column(Integer, default=1)

'''
