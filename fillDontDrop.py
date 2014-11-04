from sqlalchemy import create_engine, distinct 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime

from createTables import Base, User, IPAddress, VisitByUser, Subnet, BlockedSubnet, DontBlockSubnet
import socket
import sys

#engine = create_engine('sqlite:///sqlalchemy_sqlite.db')
engine = create_engine('mysql+mysqldb://vpn:ma93a-ya#A6@50.18.211.139:3306/vpn?charset=utf8&use_unicode=0')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

dontDrop = DontBlockSubnet(subnet="8.8.8.0/24")
session.add(dontDrop)
session.commit()

dontDrop = DontBlockSubnet(subnet="8.8.4.0/24")
session.add(dontDrop)
session.commit()

dontDrop = DontBlockSubnet(subnet="50.18.211.0/24")
session.add(dontDrop)
session.commit()


