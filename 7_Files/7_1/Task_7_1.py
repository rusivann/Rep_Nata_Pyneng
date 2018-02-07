templ1 = '''
	Protocol:              {}
	Prefix:                {}
	AD/Metric:             {}
	Next-Hop:              {}
	Last update:           {}
	Outbound Interface:    {}
'''

f = open('ospf.txt', 'r')
string_in = f.read()
f.close()
string = string_in.split()
string.remove('O')
print(templ1.format(string[0], string[1], string[2], string[3], string[4], string[5]))


