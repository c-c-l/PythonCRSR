# PYTHON3 FILE

# You have to download the BeautifulSoup library in order to use this code

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position : ')
# Convert count and position to integers
position = int(position)
count = int(count)
# Start looppage at -1 to get the first link printed too
looppage = -1
for link in url :
    looppage = looppage + 1
    if (looppage > count) :
        continue
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Follow the link x times (count) depending on their position in the page
    # Find anchor
    tags = soup('a')
    loopnum = 0
    for tag in tags :
        # Add 1 every loop 
        loopnum = loopnum + 1
        if (loopnum > position) :
            continue
        url = tag.get('href', None)
