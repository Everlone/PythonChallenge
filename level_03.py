'''
level_03.py
Python Challenge level 3
Pattern matching in strings.
'''

from re import findall

mess = open('Data/level_03.txt','r').read() 
mess = mess.replace('\n','')

text = findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',mess)

answer = ''
for char in text:
  answer += char[4]

answer += '.php'
print(answer)

