#!/usr/bin/env python3

f = open('show_arp.txt')

fl1, fl2 = False, False
mass = f.readlines()
#ip_addr, mac = ''''


for n in mass:
	ip_addr, mac = n.split()[1], n.split()[3]
	if ip_addr == '10.220.88.1':
		print('Default gateway IP/Mac = ', ip_addr, '/', mac)
		fl1 = True
	elif ip_addr == '10.220.88.30':
		print('Arista3 IP/Mac = ',  ip_addr, '/', mac)
		fl2 = True
	elif fl1 and fl2:
		break
	else:
		pass
