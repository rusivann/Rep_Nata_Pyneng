#!/usr/bin/env python3

from __future__ import print_function, unicode_literals

first_fuckinh_veriable = '2001:0db8:0000:0000:0000:0000:ae21:ad12'
The_second_fucjing_veriable = '::ae21:ad12'
The_3_rd_fucking_veriable = '::ffff:192.0.2.1'


print(first_fuckinh_veriable == The_second_fucjing_veriable)
print(first_fuckinh_veriable != The_3_rd_fucking_veriable)


##########################

show_version = "  *0        CISCO881-SEC-K9       FTX0000038X    "
show_version_stp1 = show_version.strip().split()
model, SN = show_version_stp1[1], show_version_stp1[2]
print('Cisco in model? ', 'Cisco' in model)
print('881 in the model string? ', '881' in show_version_stp1[1])
print('model - ', model, 'SN - ', SN)
