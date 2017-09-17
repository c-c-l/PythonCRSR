# PYTHON3 FILE

# This program store words of a file text in a list and
# sort the words by alphabetical order

fname = input("Enter a file name :")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line :
        if word not in lst :
            lst.append(word)
lst.sort()
print(lst)
