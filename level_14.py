from PIL import Image

length = [99]
total_length = [0]

im = Image.open("Data/level_14_wire.png")
print(im.format, im.size, im.mode)

im_new = Image.new("RGB", (100,100))
print(im_new.format, im_new.size, im_new.mode)

for i in range(0,199,2):
    length.append(length[i]-1)
    length.append(length[i]-1)
    total_length.append(total_length[i] + length[i] + 1)
    total_length.append(total_length[i+1] + length[i+1] + 1)
    

    
transforms = ([1,0], [0,1], [-1,0], [0,-1])    
count = 0
pix_x = 0
pix_y = 0



for i in range(0,199):
    current_transform = transforms[count]
    print(i, (total_length[i], total_length[i] + length[i]))
    for j in range(0,length[i]):
        pixel = im.getpixel((total_length[i] + j, 0))
        im_new.putpixel((pix_x, pix_y),pixel)
        pix_x = pix_x + current_transform[0]
        pix_y = pix_y + current_transform[1]
    if count < 3:
        count += 1
    else:
        count = 0
        
im_new.show()        
