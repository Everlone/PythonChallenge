'''
level_10.py
Python Challenge level 10
Complete series that describes elements.
Convert the string into an array of digits and identify where changes occur.
Loop over changes and separate string into blocks.
Build new string out of length and value from each block.
Append to array of series and check length of 30th element.

Better solution uses Re, but the patten is very complicated.
  for m in re.finditer(r"(\d)\1*", a): print(m)

For example:
  "".join([str(len(m[0]))+m[0][0] for m in re.finditer(r"(\d)\1*", a)])

http://www.pythonchallenge.com/pc/return/bull.html
un: huge
pw: file
'''

import numpy as np

series = ['1']

for element in range(31):
	oldstr = series[-1]
	numbers = np.array(list(map(int,oldstr)))
	change_locs = np.where(numbers[1:]-numbers[0:-1]!=0)[0] + 1
	change_locs = np.concatenate(([0],change_locs,[len(oldstr)]))

	newstr = ''
	for i in range(len(change_locs)-1):
		block = oldstr[change_locs[i]:change_locs[i+1]]
		newstr = newstr + str(len(block)) + block[0]
	print(newstr)
	series.append(newstr)

print('Answer is', len(series[30]))

