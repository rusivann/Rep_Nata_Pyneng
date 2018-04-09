#!/usr/bin/env python3
import re
f = open('show_version.txt')

ver = f.readlines()

for str in ver:
	ans = re.search('(^Cisco.*), Version (\S+), (.*$)', str)
	ans1 = re.search('^Configuration register is (.*$)', str)
	ans2 = re.search('^Processor board ID (.*$)', str)
	if ans: #если нашли строку с вхождением, то она будет не none
		print('OS Version: ', ans.group(2)) #вытаскиваем группу 2. 0-вся строка с вхождением, 1-1е скобки, 2-2е скобки и т.д.
	elif ans1:
		print('Conf reg: ', ans1.group(1))
	elif ans2:
		print('Proc ID: ', ans2.group(1))
#print(ver)

