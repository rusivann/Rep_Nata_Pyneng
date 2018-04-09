#!/usr/bin/env python3

houston_ips = ['10.10.10.1', '10.10.20.1', '10.10.30.1', '10.10.40.1', '10.10.50.1', '10.10.60.1', '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1']

atlanta_ips = ['10.10.10.1', '10.10.20.1', '10.10.30.1', '10.10.140.1', '10.10.150.1', '10.10.160.1', '10.10.170.1',
    '10.10.180.1',]

chicago_ips = ['10.10.10.1', '10.10.20.1', '10.10.140.1', '10.10.150.1', '10.10.210.1', '10.10.220.1', '10.10.230.1',
    '10.10.240.1',]


mng1 = set(houston_ips)
mng2 = set(atlanta_ips)
mng3 = set(chicago_ips)

######
# duplicated in huston and aylanta sets
print('Huston_Anlanta', mng1 & mng2)
######
# duplicated in all tree sets
print('All_tree_sets', mng1 & mng2 & mng3)
#####
# entirely unic in  Chicago
print('Unic_in_Chicago', mng3 - mng1 - mng2)
