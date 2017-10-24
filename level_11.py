from PIL import Image

im = Image.open("Data/cave.jpg")  # load image
print(im.format, im.size, im.mode) # show image details

w,h = im.size

im_even = Image.new("RGB", (w//2,h//2))
im_odd = Image.new("RGB", (w//2,h//2))

for x in range(w):
    for y in range(h):
        pixel = im.getpixel((x,y))
        if (x + y)%2 == 0:
            im_even.putpixel((x//2,y//2), pixel)
        else:
            im_odd.putpixel((x//2,y//2), pixel)


im_even.save("Data/level_11_even.png")
im_odd.save("Data/level_11_odd.png")

im_even.show()

