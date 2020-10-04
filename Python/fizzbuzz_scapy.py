#!/usr/bin/python

# *************************************************************************
#
#     This is a FizzBuz code.
#
#	  With the algorithm we generate numbers 1-100 with the corresponding 
#	  word "Fizz", "Buzz", "FizzBuzz" or the number. Then we create a 
#	  packet using scapy and we send it as a ping to a server (8.8.8.8).
#	  The reply of this ping will include a field "data" with the 
#	  desired FizzBuzz word. We pint that "data" as the output of the code.
#
#     @ecwolf
#
# *************************************************************************

from scapy.all import *
import socket

google = "8.8.8.8"  # destination IP
fizzbuzz = []  # values to be plot

# fizzbuzz algorithm
for i in range(0,101):
    if i == 0:
    	fizzbuzz.append(0)
    	continue
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz.append("FizzBuzz")
        continue
    elif i % 3 == 0:
        fizzbuzz.append("Fizz")
        continue
    elif i % 5 == 0:
    	fizzbuzz.append("Buzz")
        continue
    fizzbuzz.append(str(i))

#Senging pakets
TIMEOUT = 2
conf.verb = 0
for i in range (0,101):
    packet = IP(dst=google, ttl=20)/ICMP()/Raw(fizzbuzz[i])
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
	#Print the replied data
        print reply.load
    else:
        print "Timeout waiting for %s" % packet[IP].dst