'''
level_04.py
Python Challenge level 4
Follow links based on text strings.
Need to divide by two part way through.
Stops when there is a 'html' on the page.
'''

import urllib.request as url

nothing = '12345'
webpage = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
fingerprint = 'next nothing is '
lenfp = len(fingerprint)
trigger = True

while trigger:
	response = url.urlopen(webpage+nothing)
	page = str(response.read())
	loc = page.find(fingerprint)
	nothing = page[loc+lenfp:-1]
	if nothing=='16044': nothing = str(int(nothing)//2)
	print(nothing)
	if page.find('html')>0: trigger = False

print(page[2:-1])



