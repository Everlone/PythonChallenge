from PIL import Image

im = Image.open("Data/level_16_mozart.gif")  # load image
print(im.format,im.size,im.mode)  # show image details

xsize, ysize = im.size
search_block = [195, 195, 195, 195, 195]

im_new = Image.new("RGB", im.size)

for y in range(0, ysize-1):
    line = im.crop((0, y, xsize, y+1))
    linedat = list(line.getdata()) 
    for x in range(0, xsize-5):
        block = linedat[x:x+5]
        if block == search_block:
            part1 = im.crop((0, y, x, y+1))
            part2 = im.crop((x, y, xsize, y+1))
            im_new.paste(part2, (0, y, xsize-x, y+1))
            im_new.paste(part1, (xsize-x, y, xsize, y+1))
            
im_new.show()

im_new.save("Data/level_16_result.png")

