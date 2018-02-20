'''
level_05.py
Python Challenge level 5
Unpickle hidden file, banner.p.
Pickle requires binary so open as binary.
Rebuild pattern in lines, blocks, and individual multiples of symbols.
'''

import pickle 

stuff = pickle.load(open('Data/level_05_banner.p','rb')) 

for line in stuff:
	stringy = ''
	for nugget in line:
		stringy += nugget[0]*nugget[1]
	print(stringy)




