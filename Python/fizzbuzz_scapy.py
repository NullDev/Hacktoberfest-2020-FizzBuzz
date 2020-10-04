#!/usr/bin/python
from scapy.all import *
import socket

google = "8.8.8.8"

TIMEOUT = 2
conf.verb = 0
packet = IP(dst=google, ttl=20)/ICMP()/Raw("FIZZ")
reply = sr1(packet, timeout=TIMEOUT)
if not (reply is None):
    print reply.src, "is online"
else:
    print "Timeout waiting for %s" % packet[IP].src