import re

mess = open("Data/level_2_data.txt").read()     #  reads in all the text as a single string
print(mess)

text = re.sub('[^a-z]', '', mess)     # replaces NOT a-z with ''
print(text)


