'''
level_07.py
Python Challenge level 7
Read the graphic, strip out the grey scale line, convert 
the strip to characteris.
Resulting string contains new numbers separated by commas.
Remove space, find the []s around the numbers and extract the numbers.
'''

from PIL import Image

filename = 'Data/level_07_oxygen.png'

im = Image.open(filename)
size = im.size
im = im.crop((0,size[1]//2,size[0],size[1]//2+1))
pix = im.load()

stringy = ''
for i in range(0,size[0],7):
	if pix[i,0][0] == pix[i,0][2]:	
		stringy += chr(pix[i,0][0])

print(stringy)

stringy = stringy.replace(' ','')
numbers = stringy[stringy.find('[')+1:-1].split(',')

answer = ''
for ii in numbers:
	answer += chr(int(ii))

print(answer)


