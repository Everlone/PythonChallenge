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
