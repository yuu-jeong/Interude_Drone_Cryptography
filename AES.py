from Crypto import Random
from Crypto.Cipher import AES
import base64

BLOCK_SIZE=16

iv = "VGk6vRbcSYSgnA6CDh7ioSPuAtT7pXZarsR39rWq3bI="
cipher = "xdwG0NqU9fVwo0drfT+9rkE4Awb4YHUfQ0eqsFehfaE="
key = "YW5kcm9pZF9oYWNrZXIncw=="

class AESCryptoCBC():
   def __init__(self, iv,key):
       self.crypto = AES.new(key, AES.MODE_CBC, iv)

   def encrypt(self, data):
       enc = self.crypto.encrypt(data)
       return enc

   def decrypt(self, enc):
       dec = self.crypto.decrypt(enc)
       return dec

str6 = base64.b64decode("YW5kcm9pZF9oYWNrZXIncw==")
_decode = base64.b64decode("xdwG0NqU9fVwo0drfT+9rkE4Awb4YHUfQ0eqsFehfaE=")
bArr = [13, 112, 126, 91, 123, 29, 91, 118, 60, 11, 20, 43, 45, 127, 73, 45]
iv = bArr
key = str6
aes = AESCryptoCBC(bytes(iv), bytes(str6))
str4 = aes.decrypt(bytes(_decode))
print(str4)

decode2 = base64.b64decode("VGk6vRbcSYSgnA6CDh7ioSPuAtT7pXZarsR39rWq3bI=")
iv = bArr
#str4 = 'py0zz1tistorycom'
str4 = str4[:16]
print(str4)
aes = AESCryptoCBC(bytes(iv), bytes(str4))
print(aes.decrypt(decode2))
