#!/usr/bin/env python3
from __future__ import print_function

ip_addr = input('vvedite ip ')
ipm = ip_addr.split('.')


print('{:^15}{:^15}{:^15}{:^15}'.format('Octet1', 'Octet2', 'Octet3', 'Octet4'))
print('-' * 60)
print('{:^15}{:^15}{:^15}{:^15}'.format(ipm[0], ipm[1], ipm[2], ipm[3]))
print('{:^15b}{:^15b}{:^15b}{:^15b}'.format(int(ipm[0]), int(ipm[1]), int(ipm[2]), int(ipm[3])))
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(int(ipm[0])), hex(int(ipm[1])), hex(int(ipm[2])), hex(int(ipm[3]))))
print('-' * 60)
