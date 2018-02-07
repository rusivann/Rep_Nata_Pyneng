from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file1 = argv[1:]

fr = open(file1[0], 'r')
buff = 0

for line in fr:
    if line[0] != '!':
         for ignw in ignore:
             if ignw in line:
                 buff = 1
         if buff == 0:
             print(line.strip())         
    buff = 0





