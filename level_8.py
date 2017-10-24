import bz2  

# The b at the front is only required for python 3
# In python 2 this can be removed and the un and pw come in as str
# In python 3 there is strict seperation of test (str) and data (bytes)
# bz2 in python 3 wants data not text i.e. bytes not str
un = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

print(bz2.decompress(un))
print(bz2.decompress(pw))

