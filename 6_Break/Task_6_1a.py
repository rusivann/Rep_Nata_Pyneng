
ip = input('Vvedite ip adress: ')
ip1 = ip.split('.')
ip1 = [int(oct) for oct in ip1 if oct.isdigit()]

ip_correct = False
while not ip_correct:
	if len(ip1) != 4:
		print('nevernaya dlina, rasdelitel ili simvol')
	elif ip1[0] > 255:
		print('Incorrect octet 1')
	elif ip1[1] > 255:
        	print('Incorrect octet 2')
	elif ip1[2] > 255:
        	print('Incorrect octet 3')
	elif ip1[3] > 255:
	       	print('Incorrect octet 4')
	else :
		print('pravilniy ip')
		ip_correct = True
		continue
	ip = input('neverniy ip ')
	ip1 = ip.split('.')
	ip1 = [int(oct) for oct in ip1 if oct.isdigit()]

