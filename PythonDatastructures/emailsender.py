# PYTHON3 FILE

# This program returns the most prolific commiter

name = input("Enter file :")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = dict()

for line in handle :
    if not line.startswith('From:') : continue
    line = line.split()
    email = line[1]
    emails[email] = emails.get(email, 0) + 1
maxemailnum = 0
maxemail = None
for key in emails :
    if emails[key] > maxemailnum :
        maxemailnum = emails[key]
        maxemail = key

print(maxemail, maxemailnum)
