# PYTHON3 FILE

# This program prints out emails address from a file
# only when the line of the files starts with "From:"

fname = 'mbox-short.txt'
count = 0
fh = open(fname)
for line in fh :
    if not line.startswith('From:') : continue
    count = count + 1
    line = line.split()
    # Pattern is defined, the second word is ALWAYS an email address
    print(line[1])
print("There were", count, "lines in the files with From: as the first word")
