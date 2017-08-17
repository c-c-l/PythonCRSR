# PYTHON3 FILE

# Use the file name mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
# Line count
cl = 0
# Total value
tval = 0

for line in fh :
    if line.startswith("X-DSPAM-Confidence:") :
        cl = cl + 1
        # Get float
        idx = line.find(':')
        idx = idx + 1
        val = line[idx:]
        # Delete useless spacing
        val = val.lstrip()
        val = float(val)
        tval = tval + val
# Average
av = tval / cl
print("Average spam confidence:", av)
