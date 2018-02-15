'''
level_02.py
Python Challenge level 2
Finding unusual letters in long string.
First approach assumes I`m looking for letters.
Secondapproach uses collections.Counter to find rare characters 
'''

mess = open('Data/level_02.txt','r').read() 
# mess = mess.replace('\n','')    # this isn`t needed as \n is a single character therefore not in alpha.

alpha = 'abcdefghijklmnopqrstuvwxyz'

for char in ''.join(set(mess)):
  if alpha.find(char) == -1: 
		 mess = mess.replace(char,'')

print(mess)


''' 
Alternatively use Counter from collections to counter all the different characters.
Then isolat only the characters which are rare, i.e. occur once.
'''
from collections import Counter

mess2 = open('Data/level_02.txt','r').read()

answer = ''
chars = dict(Counter(mess2))
for ind in chars:
	if chars[ind]==1: answer += ind

answer += '.html'
print(answer)
