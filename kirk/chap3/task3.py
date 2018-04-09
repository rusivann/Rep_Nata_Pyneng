#!/usr/bin/env python3

f = open('show_lldp_neighbors_detail.txt')

mass = f.readlines()

fl1, fl2 = False, False

System_Name, Port_id, mass1 = [], [], []

for line in mass:
	if 'Port' in line.split():
		fl1 = True
		System_Name = line.split()[-1]
	elif  'System' in line.split():
		fl2 = True
		Port_id = line.split()[-1]
	elif fl1 and fl2:
		print('SystemName-{} Port id-{}'.format(System_Name, Port_id))
		break
	else:
		pass

