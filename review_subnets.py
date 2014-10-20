from sqlalchemy import create_engine, distinct 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime

from sqlalchemy_db_setup import Base, User, IPAddress, VisitByUser, Subnet, BlockedSubnet
import socket
import sys

#engine = create_engine('sqlite:///sqlalchemy_sqlite.db')
engine = create_engine('mysql+mysqldb://vpn:ma93a-ya#A6@50.18.211.139:3306/vpn?charset=utf8&use_unicode=0')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


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
