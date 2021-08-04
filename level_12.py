'''
level_12.py
Python Challenge level 12
Image contains five different graphics files interlaced, two jog, two png, and a gif.
Separate every fifth byte into a separate graphics files. 

http://www.pythonchallenge.com/pc/return/evil.html
un: huge
pw: file
'''

mess = open("Data/evil2.gfx","rb").read()          
print(mess[500:550])
print(type(mess))

picstr1 = b""
picstr2 = b""
picstr3 = b""
picstr4 = b""
picstr5 = b""

# Need to specifiy start and end of block to keep as length-1 byte 
for i in range(0,len(mess),5):
    picstr1 = picstr1 + mess[i:i+1]
    picstr2 = picstr2 + mess[i+1:i+2]
    picstr3 = picstr3 + mess[i+2:i+3]
    picstr4 = picstr4 + mess[i+3:i+4]
    picstr5 = picstr5 + mess[i+4:i+5]
    
open("Data/level_12_pic1.jpg","wb").write(picstr1)
open("Data/level_12_pic2.png","wb").write(picstr2)
open("Data/level_12_pic3.gif","wb").write(picstr3)
open("Data/level_12_pic4.png","wb").write(picstr4)
open("Data/level_12_pic5.jpg","wb").write(picstr5)

