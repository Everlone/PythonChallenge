import zipfile

file = zipfile.ZipFile("data/channel.zip", "r") # opens zipfile in "r" = read mode
     
all_comments = ""
## list file information 
#for info in file.infolist():
#    all_comments = all_comments + str(info.comment)
#    print(info.filename,info.comment)
#print(all_comments)    
#print

id_number = 90052
for item in file.infolist():   
    name = ("%s.txt" %id_number)
    data = file.read(name)
    data = (str(data)[2:-1])    # extracting string from binary
    find_location = data.find("Next nothing is")
    id_number = data[find_location + 16:]
    print(id_number, item.filename)
    x = file.getinfo(name)
    all_comments = all_comments + str(x.comment)[2]
    print(item.filename, item.comment)
    if find_location == -1:
            break

print(all_comments.replace('\\','\n'))



