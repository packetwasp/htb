from scapy.all import *

def process_packet(pkt):
    if pkt.haslayer(ICMP):
        if pkt[ICMP].type ==8:
            data= pkt[ICMP].load[-4:]
            print(f'{data.decode("utf-8")}', flush=True, end='')

sniff(iface="tun0", prn=process_packet)

