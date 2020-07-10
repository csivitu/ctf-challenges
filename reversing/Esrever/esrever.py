import random

# TODO: Remember to remove real flag before deploying
flag = 'csictf{fake_flag}'

key = 'fake_key'

def enc1(text):
    r = random.randint(1,25)
    return bytes.fromhex(''.join([hex(((ord(i) - ord('a') - r) % 26) + ord('a'))[2:] for i in text])).decode('ascii')
    
def enc2(text, key):
    k = [key[i % len(key)] for i in range(len(text))]
    return ''.join([chr(ord(text[i]) ^ ord(k[i]) + ord('a')) for i in range(len(text))])

def enc3(text):
    mapping = [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[mapping[i]] = text[i]
    
    return ''.join(temp)

def enc4(text):
    mapping = [23, 9, 5, 6, 22, 28, 25, 30, 15, 8, 16, 19, 24, 11, 10, 7, 2, 14, 18, 1, 29, 21, 12, 4, 20, 0, 26, 13, 17, 3, 27]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

encryptedText = enc1(flag)
encryptedKey = enc1(key)
for i in range(random.randint(1,100)):
    encryptedText = enc1(encryptedText)
    encryptedKey = enc1(key)

print('Encrypted Key = ' + enc4(enc4(encryptedKey)))
print('Encrypted Text = ' + enc3(enc3(enc2(enc1(encryptedText), key))))
