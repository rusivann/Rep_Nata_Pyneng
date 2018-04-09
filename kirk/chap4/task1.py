#!/usr/bin/env python3

slov = {'ip_addr': '192.168.1.1', 'vendor': 'juniper', 'username': 'odmine', 'password': 'parol'}
bgp_fields = {'bgp_as': '8271', 'peer_as': '64001', 'peer_ip': '82.123.43.45'}

##########
if slov['vendor'] == 'Cisco':
	slov.update({'platform':'ios'})
elif slov['vendor'] == 'juniper':
	slov.update({'platform':'junos'})

###########
slov.update(bgp_fields)
###########
for field in slov:
	print(field)
	print('_'*30)
##########
for key, value in slov.items():
	print('{:15} {:15}'.format(key, value))

