import pcapy
import sys
import parse_pcapy_packet
import socket
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
from sqlalchemy_db_setup import Base, User, IPAddress, VisitByUser, Subnet




def main(argv):
    dev = argv[1]

    print "dev = {}".format(dev)
    bpffilter = "ip dst {} and not src 192.168.0".format(argv[2])
    print "bpf = {}".format(bpffilter)

    engine = create_engine('mysql+mysqldb://vpn:ma93a-ya#A6@50.18.211.139:3306/vpn?charset=utf8&use_unicode=0')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    user_exists = session.query(User).filter(User.vpnUserName=='matt').all()
    if not user_exists:
        curr_user = User(fullName='Matt', vpnUserName='matt', vpnPassword='vpn_password33')
        session.add(curr_user)
        session.commit()
    else:
        curr_user = session.query(User).filter(User.vpnUserName=='matt')[0]

    

    cap = pcapy.open_live(dev, 100,1,5000)
#    cap.setfilter(bpffilter)

    cap.setfilter("not src 172.31.5.207 and not src 172.31.0.2 and not src 76.21.33.185 and not src 50.18.211.139 and not src 54.215.164.159 and not src 192.168.11.0 and not src 192.168.11.100 and not src 192.168.11.101")
    while(1):
        try:
            (header,packet) = cap.next()
#            print "header= {}".format(str(header))
#            print "packet = {}".format(packet)
#           print "packet = {}".format(packet)
            if packet:
                process_packet(packet, session, curr_user)
        except pcapy.PcapError:
            #print "pcapy error"
            pass
#           exit(-1)
        except StopIteration:
            print "cap is empty"
            exit(-1)
        except socket.timeout:
            pass

    #create capture interface
    #loop to process packets

    

def process_packet(packet, session, user):
    #parse ip_src, ip_dst
    #send to DB
    valid = True
    try:
        ip_src, ip_dst = parse_pcapy_packet.parse_packet(packet)
        #break
    except TypeError:
        print "not a valid ethernet packet"
        valid = False
    if valid:
        send_ip_db(ip_src, session, user)

count = 0

def send_ip_db(ip_src, session, user):
    global count
    hostname = "unknown host"
    try:
        hostname = socket.gethostbyaddr(ip_src)
    except socket.herror:
        hostname = "unknown"

#    print "{} : packet from ip={} : hostname={}".format(count,str(ip_src), hostname[0])
    subnet = "{}.0/24".format(ip_src.rsplit(".",1)[0])
    new_ip = IPAddress(IP=ip_src)
    new_subnet = Subnet(subnet=subnet)
    try:
        session.add(new_ip)
        session.commit()
        print "adding new ip"
    except IntegrityError:
#        print "could not add new_ip because of integrity error - {}".format(new_ip.IP)
        session.rollback()
        new_ip = session.query(IPAddress).filter(IPAddress.IP==ip_src)[0]
    try:
        session.add(new_subnet)
        session.commit()
        print "adding new subnet"
    except IntegrityError:
        session.rollback()
        new_subnet = session.query(Subnet).filter(Subnet.subnet==subnet)[0]

    new_visit = VisitByUser(user=user,IP=new_ip, subnet = new_subnet, dateTime=datetime.datetime.now())
    session.add(new_visit)
    session.commit()

    count += 1


if __name__ == "__main__":
      main(sys.argv)
