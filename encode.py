from pygost.gost3412 import GOST3412Kuznechik as gost
import hashlib
import rsa
import Crypto.Cipher.AES as aes
from Crypto.Util.Padding import pad, unpad
import json

# что шифрую
f = open('text.txt', 'rb')
text = b''
for row in f:
    text += row
text = pad(text, 32)
print(text)
# чем шифрую (ключ)
aes_key = 'password'
aes_key = aes_key.encode()
aes_key = pad(aes_key, 32)
print(aes_key)

# шифрование
obj = aes.new(aes_key, aes.MODE_ECB)
ctext = obj.encrypt(text)
print()
print(ctext)
f2 = open('ctext.txt', 'wb')
f2.write(ctext)

f.close()
f2.close()

