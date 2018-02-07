mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

for address in mac:
	address1 = address.replace(':', '.')
	print(address1)
	mac_cisco.append(address1)
print(mac_cisco)

