from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file1 = argv[1:]
fw = open('config_sw1_cleared.txt', 'w')
fr = open(file1[0], 'r')
buff = 0

for line in fr:
     for ignw in ignore:
         if ignw in line:
             buff = 1
     if buff == 0:
         fw.write(line)
     buff = 0
fw.close




