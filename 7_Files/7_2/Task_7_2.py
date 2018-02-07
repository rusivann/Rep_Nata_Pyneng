from sys import argv

file1 = argv[1:]

fr = open(file1[0], 'r')

for line in fr:
    if line[0] != '!':
         print(line.strip())


