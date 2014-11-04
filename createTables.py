from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from models import User, IPAddress, Subnet, DontBlockSubnet, VisitByUser, BlockedSubnet, Base


engine = create_engine('mysql+mysqldb://vpn:ma93a-ya#A6@50.18.211.139:3306/vpn?charset=utf8&use_unicode=0')

Base.metadata.create_all(engine)
