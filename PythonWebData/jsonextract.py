# PYTHON3 FILE
# Count comments

import urllib.request, urllib.parse, urllib.error
import json

# Get JSONFILE
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_32425.json')


# info = json.loads(fhand)

numbcomtotal = 0
for line in fhand:
    lines = line.decode().split()
    for count in lines:
        if count.startswith('"count":'):
            # Extract only the int since the pattern is always the same
            # We can just extract every line without "count:" and it
            # gives us the number
            numbcom = (count[8:len(count)])
            # Convert to int so we can add all the numbers
            numbcom = int(numbcom)
            # Add it to the total
            numbcomtotal = numbcomtotal + numbcom
print("Nombres de commentaires au total :")
print(numbcomtotal)
