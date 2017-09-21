
import os
import time



while 1:
	print "##################################################\n"
	print "Checking all devices in the network"
	os.system("fping -g 192.168.1.0/24 1>/dev/null 2>/dev/null")
	print "Checked all devices, searching ARP table.\n"	

	devices = []
	os.system("arp -a > arp.txt")
	read = open('arp.txt', 'r')
	read1 = open('arp.txt', 'r')

	
	print "Current ARP Table:\n\n"
	
	for line in read1:
			if ((line.find('incomplete'))<0):
				print line		
	for line in read:	
			if (line.find('.255') < 0):
				temp = line.partition('at')
				temp2 = temp[2]
				temp = temp2.rpartition('on')
				temp2 = temp[0]
				for i in devices:
					if i == temp2 and ((line.find('incomplete'))<0):
						print '\nARP Spoofing Detected.\n'
						print 'Relevant MAC Address: ' + temp2 + '\n'
				devices.append(temp2)

	time.sleep(5)
