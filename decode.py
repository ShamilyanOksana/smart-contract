from pygost.gost3412 import GOST3412Kuznechik as gost
import hashlib
import rsa
import Crypto.Cipher.AES as aes
from Crypto.Util.Padding import pad, unpad
import json

aes_key = 'password'
aes_key = aes_key.encode()
aes_key = pad(aes_key, 32)
print(aes_key)

with open('ctext.txt', 'rb') as cf:
    ctext = cf.readline()

print(ctext)
obj = aes.new(aes_key, aes.MODE_ECB)
text = obj.decrypt(ctext)
print(text)

text = unpad(text, 32)
with open('new.txt', 'wb') as f:
    f.write(text)






