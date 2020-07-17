from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import binascii
import sys

key = get_random_bytes(16)
iv = get_random_bytes(16)
flag="csictf{Sh4u!d_hav3_n0t_u5ed_CBC}"

def encrypt(str1):
    obj = AES.new(key, AES.MODE_CBC, iv)
    str1=str1.encode('utf-8')
    str1 = pad(str1,16)
    ciphertext = obj.encrypt(str1)
    return ciphertext

def decrypt(str2):
    obj=AES.new(key, AES.MODE_CBC, iv)
    plaintext=obj.decrypt(str2)
    plaintext=unpad(plaintext,16)
    return plaintext


print("We implemented a really cool AES-encryption for our login, however in the process we forgot the username and password to the admin account.")
sys.stdout.flush()
print("We don't remember the exact credentials but the username was similar to c?i and password similar to c?f.")
sys.stdout.flush()
print("When we entered 'user:c?i' and 'pass:c?f' the portal spit out 2 hex strings : ")
sys.stdout.flush()
enc1=encrypt("user:c?i")
enc2=encrypt("pass:c?f")
hexstring1=binascii.hexlify(enc1)
hexstring2=binascii.hexlify(enc2)
print()
sys.stdout.flush()
print(str(binascii.hexlify(iv))[2:-1]+str(hexstring1)[2:-1])
sys.stdout.flush()
print(str(binascii.hexlify(iv))[2:-1]+str(hexstring2)[2:-1])
sys.stdout.flush()
print()
sys.stdout.flush()
print("The only way to login now is to enter 2 hex strings which decrypt to the correct credentials.")
sys.stdout.flush()

try:
    inp1=input('Enter username hex string : ')
    inp2=input('Enter password hex string : ')
    inp1.encode('utf-8')
    inp2.encode('utf-8')
    inp1=binascii.unhexlify(inp1)
    inp2=binascii.unhexlify(inp2)
    dec1=decrypt(inp1)
    dec1=str(dec1)[2:-1]
    dec2=decrypt(inp2)
    dec2=str(dec2)[2:-1]
    if("user:csi" in dec1 and "pass:ctf" in dec2):
        print("Congratulations u fixed our problems, here is the flag : ",flag)
    else:
        print("Not even close")
except:
    print("Error!!")
