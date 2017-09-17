# PYTHON3 FILE

name = input("Enter file:")
if len(name < 1 : name = "mbox-short.txt")
handle = open(name)
counts = dict()
for line in handle :
    line = line.rstrip()
    if not line.startswith('From') : continue
    line = line.split()
    if len(line) > 2 :
        time = line[5]
        hour = time.split(':')
        hour = hour[0]
        counts[hour] = counts.get(hour, 0) + 1
lst = list()
for k, v in counts.items() :
    tup = (k, v)
    lst.append(tup)
lst = sorted(lst)
for v, k in lst :
    print(v, k)
