import socket

def get_host(ip):

    hostname = "No DNS Resolution"
    if len(ip.split(".")) == 3:
        ip = "{}.1".format(ip)
#    print "ip = {}".format(ip)
    try:
        hostname = socket.gethostbyaddr(ip)
    except socket.herror:
        return False
        print "could not resolve {}".format(ip)
    return hostname



