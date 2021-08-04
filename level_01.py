'''
level_01.py
Python Challenge level 1
Cipher letters using maketrans (as recommended in decoded text)

http://www.pythonchallenge.com/pc/def/274877906944.html
'''

msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alpha = "(). abcdefghijklmnopqrstuvwxyz"
beta = "(). cdefghijklmnopqrstuvwxyzab"

print(msg.translate(msg.maketrans(alpha,beta)))

url = 'map'
print(url, 'becomes', url.translate(msg.maketrans(alpha,beta)))


