fr = open('CAM_table.txt', 'r')

for line in fr:
    if 'DYNAMIC' in line:
       line = line.split() 
       line.remove('DYNAMIC')
       print("   {:}   {:}   {:}  ".format(line[0], line[1], line[2]))
