import json
import urllib

#input = 'http://python-data.dr-chuck.net/comments_42.json'
input = 'http://python-data.dr-chuck.net/comments_287116.json'
data = urllib.urlopen(input).read()
#print 'data: ', data

info = json.loads(str(data))
#print 'info: ', info
#print 'length info: ', len(info)
#print json.dumps(info, indent = 4)
#print info['comments'][0]['count']
sum = 0
for item in info['comments']:
    print item['count']
    sum = sum + int(item['count'])
print "sum: ", sum
