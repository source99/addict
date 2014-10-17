import pcapy
import sys
import parse_pcapy_packet
import socket
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
from sqlalchemy_db_setup import Base, User, IPAddress, VisitByUser




def main(argv):
    dev = argv[1]

    print "dev = {}".format(dev)
    bpffilter = "ip dst {} and not src 192.168.0".format(argv[2])
    print "bpf = {}".format(bpffilter)

    engine = create_engine('sqlite:///sqlalchemy_sqlite.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    new_user = User(fullName='Matt', vpnUserName='matt', vpnPassword='vpn_password33')
    session.add(new_user)
    session.commit()

    

    cap = pcapy.open_live(dev, 100,1,5000)
    cap.setfilter(bpffilter)
    while(1):
        try:
            (header,packet) = cap.next()
#           print "packet = {}".format(packet)
            if packet:
                process_packet(packet, session, new_user)
        except pcapy.PcapError:
            #print "pcapy error"
            pass
#           exit(-1)
        except StopIteration:
            print "cap is empty"
            exit(-1)

    #create capture interface
    #loop to process packets

    

def process_packet(packet, session, user):
    #parse ip_src, ip_dst
    #send to DB
    try:
        ip_src, ip_dst = parse_pcapy_packet.parse_packet(packet)
        send_ip_db(ip_src, session, user)
        #break
    except TypeError:
        print "not a valid ethernet packet"

count = 0

def send_ip_db(ip_src, session, user):
    global count
    hostname = "unknown host"
    try:
        hostname = socket.gethostbyaddr(ip_src)
    except socket.herror:
        print "could not lookup {}".format(ip_src)

    print "{} : packet from ip={} : hostname={}".format(count,str(ip_src), hostname[0])
    subnet = ip_src.rsplit(".",1)[0]
    new_ip = IPAddress(IP=ip_src, subnet=subnet)
    try:
        session.add(new_ip)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_ip = session.query(IPAddress).filter(IPAddress.IP==ip_src)[0]
    new_visit = VisitByUser(user=user,IP=new_ip, dateTime=datetime.datetime.now())
    session.add(new_visit)
    session.commit()

    count += 1


if __name__ == "__main__":
      main(sys.argv)
