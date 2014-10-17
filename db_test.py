from sqlalchemy import create_engine, distinct 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime

from sqlalchemy_db_setup import Base, User, IPAddress, VisitByUser
import socket
import sys

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

#exit(-1)

IPs = session.query(IPAddress).all()
for IP in IPs:
    print "IP = {} : subnet = {}".format(IP.IP, IP.subnet)

#visits = session.query(VisitByUser).all()
#for visit in visits:
#    print "visit: userid = {}, IPID = {}, datetime={}".format(visit.userID, visit.IPID, visit.dateTime)


#print "len of IP = {}, len of visits = {}".format(len(IPs), len(visits))
#unique_subnets = session.query(distinct(IPAddress.subnet)).all()


subnets = session.query(distinct(IPAddress.subnet)).all()
#subnets = session.query(IPAddress.subnet).all()
def get_host(ip):

    hostname = "No DNS Resolution"
    if len(ip.split(".")) == 3:
        ip = "{}.1".format(ip)
    try:
        hostname = socket.gethostbyaddr(ip)
    except socket.herror:
        print "could not resolve {}".format(ip)
    return hostname

ignore_hosts = []
import fileinput
for subnet in subnets:
    subnet = subnet[0].encode("ascii")
    hostname = get_host(subnet)
    print "\nDo you want to block {} : {}".format(subnet, hostname)
    answer = sys.stdin.readline().upper()
    if "Y" in answer:
        print "saving {} {} to DB".format(hostname, subnet)
        ignore_hosts.append(subnet)



for ip in ignore_hosts:
    print "{}".format(ip)
