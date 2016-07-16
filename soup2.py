import re
import urllib
from BeautifulSoup import *
#html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
html = urllib.urlopen('http://python-data.dr-chuck.net/comments_287115.html').read()

#print 'html \n', html
soup = BeautifulSoup(html)
#print 'soup \n', soup
# Retrieve all of the anchor tags
tags = soup('span')
#print 'tags\n', tags
sum = 0
for tag in tags:
   # Look at the parts of a tag
   numlist = re.findall('>([0-9]+)<', str(tag))
   sum = sum + int(numlist[0])
   #print 'TAG:', tag
   #print 'sum:', sum
print sum
