from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime

from sqlalchemy_db_setup import Base, User, IPAddress, VisitByUser


engine = create_engine('sqlite:///sqlalchemy_sqlite.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(fullName='Allison Sigmond', vpnUserName='asigmond', vpnPassword='vpn_password33')
session.add(new_user)
session.commit()

new_ip = IPAddress(IP="128.2.10.10", subnet="128.2.10.0")
try:
    session.add(new_ip)
    session.commit()
except IntegrityError:
    session.rollback()
    print "IP already in DB"
    new_ip = session.query(IPAddress).filter(IPAddress.IP=="128.2.10.10")[0]
    

print "new_user = {}".format(new_user.fullName)
print "new_ip = {}".format(new_ip.IP)
dateTime =datetime.datetime.now()
print "dateTime = {}".format(dateTime)
new_visit = VisitByUser(user=new_user, IP = new_ip, dateTime=dateTime)
session.add(new_visit)
session.commit()

users = session.query(User).all()
for user in users:
    print "User = {}".format(user.fullName)

IPs = session.query(IPAddress).all()
for IP in IPs:
    print "IP = {} : subnet = {}".format(IP.IP, IP.subnet)

visits = session.query(VisitByUser).all()
for visit in visits:
    print "visit: userid = {}, IPID = {}, datetime={}".format(visit.userID, visit.IPID, visit.dateTime)
