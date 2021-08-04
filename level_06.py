'''
level_06.py
Python Challenge level 6
Opening a zip file containing a huge number of files to link through
like the linked list.
The readme file says to start from 90052.
Comments are collected and include \\ and n which needs to be replaced with \n.
This allows the printing to seperated the obtained lines.

http://www.pythonchallenge.com/pc/def/channel.html
'''

from zipfile import ZipFile

nothing = '90052'
fingerprint = 'ext nothing is '
lenfp = len(fingerprint)

myzip = ZipFile('Data/level_06_channel.zip') 
print(myzip.read('readme.txt'))

comments = ''
while True:
    try:
        string = str(myzip.read(nothing + '.txt'))
    except: 
        break
    comments = comments + str(myzip.getinfo(nothing + '.txt').comment)[2:-1]
    loc = string.find(fingerprint)
    nothing = string[loc + lenfp:-1]
    print(nothing)

print(comments.replace('\\n','\n'))
