'''
level_15.py
Python Challenge level 15
Find a person related to January 26th in a year between 1006 and 1996 (based on image),
where the January starts on a Thursday.
This limits me to a selection of years, and a Google search reveals Mozart.

http://www.pythonchallenge.com/pc/return/cat.html
http://www.pythonchallenge.com/pc/return/uzi.html
un: huge
pw: file
'''

import calendar

start_day = 3

year_list = []

for i in range(2000,1000,-4):
    if calendar.weekday(i,1,1) == start_day:
        if str(i)[3] == '6':
            year_list.append(str(i))
        
print(year_list)        

print('Google search reveals mozart was born on 26 January 1756')
print('Lame Puzzle!!')
