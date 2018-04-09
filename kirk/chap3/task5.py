#!/usr/bin/env python3
import os
mass = []
for n in range (1,255):
	mass.append('172.17.4.' + str(n))
for m,k in enumerate(mass):
	print(m, '--->', k)

### slicing mass

mass1 = mass[2:6]

print(mass1)

for n in mass1:
	os.system('ping -c 3 ' + n) 

