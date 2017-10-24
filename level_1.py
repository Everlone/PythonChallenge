alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = "cdefghijklmnopqrstuvwxyzab"

code_table = str.maketrans(alphabet,cipher)

print("\r")
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print("message = ", message)

print("\r")
decoded = str.translate(message,code_table)
print("decoded message = ", decoded)

print("\r")
message = "map"
print("url = ", message)

print("\r")
decoded = str.translate(message,code_table)
print("decoded url = ", decoded)

