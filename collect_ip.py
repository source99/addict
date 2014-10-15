import pcapy
import sys
import parse_pcapy_packet
import socket

def main(argv):
	dev = argv[1]

	print "dev = {}".format(dev)
	bpffilter = "ip dst {} and not src 192.168.0".format(argv[2])
	print "bpf = {}".format(bpffilter)

	cap = pcapy.open_live(dev, 100,1,5000)
	cap.setfilter(bpffilter)
	while(1):
		try:
			(header,packet) = cap.next()
#			print "packet = {}".format(packet)
			if packet:
				process_packet(packet)
		except pcapy.PcapError:
			#print "pcapy error"
			pass
#			exit(-1)
		except StopIteration:
			print "cap is empty"
			exit(-1)

	#create capture interface
	#loop to process packets

	

def process_packet(packet):
	#parse ip_src, ip_dst
	#send to DB
	try:
		ip_src, ip_dst = parse_pcapy_packet.parse_packet(packet)
		send_ip_db(ip_src, ip_dst)
		#break
	except TypeError:
		print "not a valid ethernet packet"

count = 0

def send_ip_db(ip_src, ip_dst):
	global count
	hostname = "unknown host"
	try:
		hostname = socket.gethostbyaddr(ip_src)
	except socket.herror:
		print "could not lookup {}".format(ip_src)

	print "{} : packet from ip={} : hostname={}".format(count,str(ip_src), hostname[0])
	count += 1


if __name__ == "__main__":
	  main(sys.argv)
