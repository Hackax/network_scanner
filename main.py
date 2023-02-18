import scapy.all as scapy
import sys

args = sys.argv

def arp_ping_scan(ip):
    scapy.arping(ip)

def ARP_scan(ip):
    arp_request = scapy.ARP(pdst=ip) # Creating a ARP packet to map the mac address on each 'ip'.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Creating a Ethernet frame with broadcast destination mac address 'ff:ff:ff:ff:ff:ff'.
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    print("IP Address | MAC Address")
    for x in answered:
        print(f"{x.answer.psrc} | {x.answer.hwsrc}")



if __name__ == "__main__":

    try:
        if args[1] == "-ip":
            ARP_scan(args[2])

        elif args[1] == "-arping":
            print(scapy.arping(args[2]))

    except:
        print("USAGE: python main.py (-ip/-arping) [ip_address]")
