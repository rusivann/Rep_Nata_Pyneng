#!/usr/bin/env python3
import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.'
Processor board ID FTX0000038X
'''

line = show_version

mach = re.search('^Cisco (?P<model>\S+).* with (?P<memory>\S+) bytes of memory', line, flags=re.M)


print('Cisco model --> ', mach.groupdict()['model'])
print('Cisco memory --> ', mach.groupdict()['memory'])
print('-'*100)

#####################
# sandbox section
mach1 = re.search('^Cisco.*', line, flags=re.M)
print(mach1)
