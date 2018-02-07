fr = open('CAM_table.txt', 'r')

mass = []
buff = []
vlan = input('vvedite vlan - ')

for line in fr:
    if 'DYNAMIC' in line:
       line = line.split() 
       line.remove('DYNAMIC')
       mass.append(line)

#for i in range(len(mass)):
#    for j in range(len(mass) - 1):
#        if mass[j][0] > mass[j + 1][0]:
#            buff = mass[j][0]
#            mass[j][0] = mass[j + 1][0]
#            mass[j + 1][0] = buff

for step in range(len(mass)):
    if mass[step][0] == vlan:
        print("   {:}   {:}   {:}  ".format(mass[step][0], mass[step][1], mass[step][2]))
