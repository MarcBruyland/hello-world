import urllib
from BeautifulSoup import *
html = urllib.urlopen('http://www.dr-chuck.com/page1.htm').read()
print 'html \n', html
soup = BeautifulSoup(html)
print 'soup \n', soup
tags = soup('a')
print 'tags\n', tags
for tag in tags:
  print 'tag\n', tag.get('href', None)
