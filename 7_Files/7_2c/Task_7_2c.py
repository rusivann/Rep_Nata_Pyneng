from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

input, output = argv[1:]

fr = open(input, 'r')
fw = open(output, 'w')
buff = 0

for line in fr:
     for ignw in ignore:
         if ignw in line:
             buff = 1
     if buff == 0:
         fw.write(line)
     buff = 0
fw.close




