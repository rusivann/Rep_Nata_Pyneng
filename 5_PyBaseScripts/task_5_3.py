
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

variant_voprosa_acc = 'Enter VLAN number: '
variant_voprosa_tru = 'Enter allowed VLANs: '


############

porttype = input('Vevedite regim porta: ')
portname = input('Vvedite tip&nomer porta: ')

tuple1 = {'access': access_template, 'trunk': trunk_template}
tuple2 = {'access': variant_voprosa_acc, 'trunk': variant_voprosa_tru}
inputvlan = input(tuple2[porttype])

print('interface {}'.format(portname))
print('\n'.join(tuple1[porttype]).format(inputvlan))
