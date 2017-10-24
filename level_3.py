import re

mess = open("data/level_3_data.txt").read()     #  reads in all the text as a single string
print(mess)

clean = re.findall('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', mess)     # searches for matches to a aAAAzAAAa 
                                                                              # and returns the z
text = ""
for str in clean:
    text += str[4]
print(text)

