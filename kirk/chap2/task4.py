#!/usr/bin/env python3
with open('show_ip_int_brief.txt') as f:
	mass = f.readlines()

fa4 = mass[-2]
print(fa4)
