#!/bin/bash 

#bits = sys.argv[1]
#host_bits = 32 - int(bits)
#total_addr = 2**host_bits
#usable_addr = total_addr - 2
#print "address: " + str(total_addr) + " usable: " + str(usable_addr) + " netmask: " 

#ip route | grep 'default via' | awk 'BEGIN {ORS=" "} {print "gateway: "$3}' 

#ifconfig | grep 'Bcast' | cut -d: -f4 | awk 'BEGIN {ORS=" "} {print "netmask: " $1}' 

#ip route | grep 'default via' | awk '{print "device: " $5}' 

echo -e "gateway: $(ip r | grep default | cut -d " " -f3) netmask: $(ifconfig | grep -o 'netmask.*'|head -1 | cut -d ' ' -f2) device: $(ip r | tail -1 | cut -d ' ' -f3)"
