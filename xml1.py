import urllib
import xml.etree.ElementTree as ET

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_287112.xml'

data =  urllib.urlopen(url).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

sum = 0
for cnt in counts:
    sum = sum + int(cnt.text)
    print cnt.text, sum
