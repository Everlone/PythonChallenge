import xmlrpc.client            # access xml remote procedure call

mess = open("Data/evil4.jpg","rb").read()    # infomation for level 13, hidden in level 12
print(mess)

url = "http://www.pythonchallenge.com/pc/phonebook.php"

phonebook = xmlrpc.client.ServerProxy(url)    # create inastance of Server Access

print(phonebook.system.listMethods())     # show methods available to instance

print(phonebook.system.methodHelp("phone"))    # show help for method "phone"

print(phonebook.system.methodSignature("phone"))    # show signature for method "phone"

print(phonebook.phone("Bert"))         # use phone method
