#!/usr/bin/env python3
from __future__ import print_function


mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1m = mac1.split()
mac2m = mac2.split()
mac3m = mac3.split()

print('{:>20} {:>20}'.format('IP ADDR', 'MAC ADDRESS'))
print('{:>20} {:>20}'.format('-' * 20, '-' * 20))
print('{:>20} {:>20}'.format(mac1m[1], mac1m[3]))
print('{:>20} {:>20}'.format(mac2m[1], mac2m[3]))
print('{:>20} {:>20}'.format(mac3m[1], mac3m[3]))
