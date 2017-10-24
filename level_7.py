from PIL import Image  # import python imaging library (pillow 2.2.1 library)

im = Image.open("data/level_7_oxygen.png")  # load image
print(im.format, im.size, im.mode) # show image details
x=im.size                       
print(x[0],x[1])              # show image width and height
y=round(x[1]/2)             # grey bar is at half height
imc=im.crop([0,y-1,x[0],y])  # crop image to a single line
print(imc.size)
imdat=list(imc.getdata())    # list turns imc.getdata into a format
                            # that can be used outside of the PIL

z=""                        
for i in range(0,x[0],7):        # grey blocks are 7 pixels long
    if imdat[i][0] == imdat[i][1]:   # only examine grey bar, not picture at end of bar
        z += chr(imdat[i][0])    # turn grey bar into ascii
print(z)                          # show answer

z=""
codey = [105, 110, 116, 101, 103, 114, 105, 116, 121]   # code from answer
for char in codey:
    z += chr(char)         # convert code to ascii
print(z)               # show next page
    


