import re
import urllib
from BeautifulSoup import *


#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
#count = 4
#pos = 3
url = 'http://python-data.dr-chuck.net/known_by_Kaycee.html'
count = 7
pos = 18
print 'count = ', count
print 'pos = ', pos
print url

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    j = 0
    for tag in tags:
       #print 'TAG:', tag
       j = j + 1
       if j == pos:
           url = tag.get('href', None)
           print url
