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


subnets = session.query(distinct(Subnet.subnet)).all()
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

ignoreHosts = []

dontBlockSubnetsList = session.query(DontBlockSubnet).all()
#print dontBlockSubnetsList
for subnet in dontBlockSubnetsList:
#    print subnet.subnet
    ignoreHosts.append(subnet.subnet)

for subnet in subnets:
    subnet = subnet[0].encode("ascii")
    if not subnet in ignoreHosts:
        print "sudo iptables -A PREROUTING -t mangle -i eth0 -s {}  -j MARK --set-mark 11".format(subnet)
    

exit(-1)








for subnet in subnets:
    subnet = subnet[0].encode("ascii")
    ip = subnet.replace(".0/24",".1")
    print "ip = {}".format(ip)
    hostname = get_host(ip)
    print "\nDo you want to block {} : {}".format(subnet, hostname)
    answer = sys.stdin.readline().upper()
    if "Y" in answer:
        print "saving {} {} to DB".format(hostname, subnet)
        ignore_hosts.append(subnet)



for ip in ignore_hosts:
    print "{}".format(ip)
