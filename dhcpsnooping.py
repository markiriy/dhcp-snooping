import csv
import re


def write_dhcp_snooping_to_csv(filenames, output):
    lines = []
    newlines = []
    nono = 'dhcp-snooping'
    name = filenames.split("_")
    f = open(filenames, 'r')
    readfile = f.read().split('\n')
    print(readfile)
    for el in range(2, len(readfile)-1):
        newtxt = re.sub("[^\S\r\n]+", ",", readfile[el].strip())
        lines.append(newtxt)
    for s in lines:
        s = s.split(',')
        newlines.extend(s)
    csv_out = csv.writer(open(output, 'w'), delimiter=',')
    csv_out.writerow(('switch', 'mac', 'ip', 'vlan', 'interface'))
    for i in newlines:
        if i == nono:
            newlines.remove('dhcp-snooping')
        else:
            continue
    for j in range(0, len(newlines)):
        if j % 5 == 0:
            csv_out.writerow((name[0], newlines[j], newlines[j+1], newlines[j+3], newlines[j+4]))
    f.close()


write_dhcp_snooping_to_csv('sw1_dhcp_snooping.txt', 'sw1_dhcp_snooping_csv.csv')