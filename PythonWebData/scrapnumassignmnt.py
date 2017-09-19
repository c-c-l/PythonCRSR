# PYTHON3 FILE

# You have to download the BeautifulSoup library in order to use this code

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_32422.html'
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all numbers of comments on the page
# This is hardcoded because comments are located
# in the "span" tag and it is not used elsewhere
tags = soup('span')
numcom = 0
comments = list()
for tag in tags :
    # Add 1 every comment 
    numcom = numcom + 1
    # Get content of tag aka number
    cnt = tag.contents[0]
    # Convert the content to a int to use sum()
    cnt = int(cnt)
    # Add the int to the list
    comments.append(cnt)
    total = sum(comments)
print(numcom)
print(total)
