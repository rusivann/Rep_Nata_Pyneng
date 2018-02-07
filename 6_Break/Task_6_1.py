ip = input('Vvedite ip adress: ')
ip1 = ip.split('.')
ipmark = int(ip1[0])

if (ipmark < 224) & (ipmark >= 1):
	print('unicast')
elif (ipmark <= 239) & (ipmark >= 224):
	print('multycast')
elif ip == '255.255.255.255':
	print('local broadcast')
elif ip == '0.0.0.0':
	print('unassigned')
else:
	print('unused')
