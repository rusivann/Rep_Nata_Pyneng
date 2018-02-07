print('vvedite adress and mask')
from sys import argv
ip = argv[1]

ip1 = ip.split('/')
ip2 = ip1[0]
ip3 = ip2.split('.')
mask = ip1[1]

ipe0 = ('0'*8 + (bin(int(ip3[0]))[2:]))[-8:]
ipe1 = ('0'*8 + (bin(int(ip3[1]))[2:]))[-8:]
ipe2 = ('0'*8 + (bin(int(ip3[2]))[2:]))[-8:]
ipe3 = ('0'*8 + (bin(int(ip3[3]))[2:]))[-8:]
ipbin = ((((ipe0 + ipe1 + ipe2 + ipe3)[0:int(mask)])) + '0'*32)[0:32]

ip3 = [int(ipbin[0:8], 2), int(ipbin[8:16], 2),int(ipbin[16:24], 2),int(ipbin[24:32], 2)]

maskbin = (int(mask)) * '1' + (32 - (int(mask))) * '0'
masklist = [maskbin[0:8], maskbin[8:16], maskbin[16:24], maskbin[24:32]]

template222 = '''
	network: 

	{:<8} {:<8} {:<8} {:<8}
	{:08b} {:08b} {:08b} {:08b}
	mask: 

	/{}
'''
template333 = '''
	{:<8} {:<8} {:<8} {:<8}
	{:<8} {:<8} {:<8} {:<8}
'''	


print(template222.format(ip3[0], ip3[1], ip3[2], ip3[3], int(ip3[0]), 
int(ip3[1]), int(ip3[2]), int(ip3[3]), mask))

print(template333.format(int(masklist[0], 2), int(masklist[1], 2), int(masklist[2], 2), 
int(masklist[3], 2), masklist[0], masklist[1], masklist[2], masklist[3]))


