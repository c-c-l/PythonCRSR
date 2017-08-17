# PYTHON3 FILE

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
for line in inp :
    # Delete double newline
    line = mine.rstrip()
inp = inp.upper()
print(inp[:])
