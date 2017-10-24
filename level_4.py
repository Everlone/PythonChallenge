import urllib.request

#id_number = "12345"
id_number = "8022"
loop_flag = 1

while loop_flag == 1:
    address = ("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" %id_number)
    fp = urllib.request.urlopen(address)
    s = fp.read(8192)
    if not s:
        break
    print(s)
    find_location = str(s).find("the next nothing is")
    if find_location == -1:
        loop_flag = 0
        break
    id_number = str(s)[find_location+20:]
    print(id_number)
    fp.close()




