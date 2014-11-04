from sqlalchemy import create_engine, distinct 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime

from createTables import Base, User, IPAddress, VisitByUser, Subnet, BlockedSubnet, DontBlockSubnet
import socket
import sys
from utils import get_host

engine = create_engine('mysql+mysqldb://vpn:ma93a-ya#A6@50.18.211.139:3306/vpn?charset=utf8&use_unicode=0')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


ignoreHosts = []
dontBlockSubnetsList = session.query(DontBlockSubnet).all()
for subnet in dontBlockSubnetsList:
    ignoreHosts.append(subnet.subnet)

IPs = session.query(distinct(IPAddress.IP)).all()

auto_block = [
        "twttr",
        "akamai",
        "fbcdn",
        "facebook",
        "1e100"
        ]


for IP in IPs:
    host = get_host(IP[0])
    if host:
        host = host[0]
        auto_block_bool = False
        for blocker in auto_block:
            if blocker in host:
                print "autoblocking : {} : {}".format(IP[0], get_host(IP[0]))
                auto_block_bool = True
        if not auto_block_bool:
            print "unknown : {} : {}".format(IP[0], get_host(IP[0]))
    else:
        print "could not resolve : {}".format(IP[0])


exit(-1)



for IP in IPs:
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
