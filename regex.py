import re

name = raw_input("Enter file:")
#if len(name) < 1 : name = "regex_sum_42.txt"
if len(name) < 1 : name = "regex_sum_287110.txt"
handle = open(name)

text = handle.read()
numlist = re.findall('([0-9]+)\s', text)
sum = 0
for num in numlist:
    sum = sum + int(num)
#    print num, sum
print sum
