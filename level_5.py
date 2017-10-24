import pickle

mess = open("data/level_5_banner.p").read()     #  reads in all the text as a single string
# print(mess)

mess = str.encode(mess)    # convert string to bytes ready for pickle
decoded = pickle.loads(mess)
print(decoded)

strip = ""
for line in decoded:
    # print line
    print(strip)
    strip = ""
    for blob in line:
        # print blob
        for bit in blob:
            # print bit
            if type(bit) == int:
                bit_number = bit
                strip = strip + (bit_string*bit_number)
            else:
                bit_string = bit
     
                
