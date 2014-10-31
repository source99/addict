import os
import sys
from subprocess import call, Popen



def call_command(command):
    print command
    call(command, shell=True)

if __name__ == "__main__":
    try:
        os.rename('/etc/check_root', '/etc/bar')
        os.rename('/etc/bar', '/etc/check_root')
    except OSError:
            print "Please run this as root"
            exit(-1)
    if len(sys.argv) != 3:
        print "sudo python create_user.py USERNAME EMAIL"
        exit(-2)
    username = sys.argv[1]
    email = sys.argv[2]

    keyPath = "/etc/ipsec.d/private/"
    keyName = "{}Key.pem".format(username)
    keyFull = "{}{}".format(keyPath, keyName)
    certFull = "/etc/ipsec.d/certs/{}Cert.pem".format(username)
    caFull = "/etc/ipsec.d/cacerts/strongswanCert.pem"
    hostFullKey = "/etc/ipsec.d/private/strongswanKey.pem"
    p12path = "/etc/ipsec.d/p12/"
    p12full = "{}/{}.p12".format(p12path, username)
    mobileconfigFilename = "{}.mobileconfig".format(username)


    #create key
    command = "ipsec pki --gen --type rsa --size 2048 --outform pem > {}".format(keyFull)
    call_command(command)
    command = "chmod 600 {}".format(keyFull)
    call_command(command)
    #sign key with CA
    command = "ipsec pki --pub --in {} --type rsa | ipsec pki --issue --lifetime 730 --cacert {} --cakey {} --dn \"C=CH, O=strongSwan, CN={}\" --san {} --outform pem > {}".format(keyFull, caFull, hostFullKey, email, email, certFull)
    call_command(command)

    command = "openssl pkcs12 -export -inkey {} -in {} -name \"{}'s VPN Certificate\" -certfile {} -caname \"strongSwan Root CA\" -out {}".format(keyFull, certFull, username, caFull, p12full)
#    print "use this as password {}_vpn_password33".format(username)
    call_command(command) 
#    print "mkdir /Users/matt/work/addict/keys/{}".format(username)
#    print "scp -i /Users/matt/work/addict/key_pairs/vpn_west.pem ubuntu@strong.lesstechmorepeople.com:{} /Users/matt/work/addict/keys/{}/".format(p12full, username)
#    print "scp -i /Users/matt/work/addict/key_pairs/vpn_west.pem ubuntu@strong.lesstechmorepeople.com:{} /Users/matt/work/addict/keys/{}/strongswanCert.crt\n".format(caFull, username)

    #make full p12
    command = "python /home/ubuntu/addict/makeMobileconfig.py {} {} {} {}".format(username, email, p12full, mobileconfigFilename)
    call_command(command)   
    command = "scp -i /home/ubuntu/addict/addict_web.pem {} ubuntu@www.lesstechmorepeople.com:/var/www/profile/{}".format(mobileconfigFilename, mobileconfigFilename)
    call_command(command)
    #copy somewhere
	


