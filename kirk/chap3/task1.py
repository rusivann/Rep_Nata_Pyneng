#!/usr/bin/env python3

f = open('show_vlan.txt')
spis = (f.readlines())
n2 = []

for n in spis:
     n1 = n.split()
     if (n1[0] == 'VLAN') and (n1[1] == 'Name'):
         pass
     elif ('-' in n1[0]):
         pass
     elif 'Et' in n1[0]:
        pass
     else:
         n2.append((n1[0], n1[1]))

print(n2)
