#HW4: networking


import sys


addresses = 1 
index = 32              #squares


netmask_1, netmask_2, netmask_3 = 255, 255, 255 #constant
counter_2,counter_3 = 1, 1
netmask_4 = 0

for i in range(24): #will go through the adress 
    addresses *= 2
    index -= 1
    
    if(index >= 24 and index<=31): #the number of bits 24-31
        netmask_4 = 256 - addresses
        
    if(index >=16 and index <= 23): #the number of bits 16-23
        counter_3 *= 2
        netmask_3 = 256 - counter_3
        
    if(index >=8 and index <=15):    #the number of bits 8-15
        counter_2 *= 2
        netmask_2  = 256 -counter_2
        
    if(index == int(sys.argv[1])):
        print("addresses: ",addresses, " usable: ", (addresses - 2), " ","netmask: ", netmask_1, ".", netmask_2,".", netmask_3,".",netmask_4, sep = "")
        exit()
