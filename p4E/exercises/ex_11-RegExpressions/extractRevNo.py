#search for line that start with 'Details: rev='
#followed by numbers
#then print the numbers if one is found.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print(x)