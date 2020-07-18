import random 
import sys

map = ['v', 'r', 't', 'p', 'w', 'g', 'n', 'c', 'o', 'b', 'a', 'f', 'm', 'i', 'l', 'u', 'h', 'z', 'd', 'q', 'j', 'y', 'x', 'e', 'k', 's']

flag = 'csictf{this_is_a_fake_flag}'
flag = flag.replace('{','a')
flag = flag.replace('}','a')
flag = flag.replace('_','b')
key1 = 'ashikka_is_mine'
key1 = key1.replace('_','b')

if(len(flag) != 28 or len(key1) != 14):
    exit()
    
flag = list(flag)
key1 = list(key1)


def enc1(text):
    n = random.randint(0,sys.maxsize%28)
    return text[n:] + text[:n]
    
flag = enc1(flag)
    
def enc2(text):
    temp = ''
    for i in text:
        temp += map[ord(i)-ord('a')]
    return temp

key2 = enc2(enc2(key1))
key2 = list(key2)

for j in range(2):
    for i in range(14):
        temp1 = flag[i]
        flag[i] = flag[(ord(key1[i])-ord('a'))%28] 
        flag[(ord(key1[i])-ord('a'))%28] = temp1
        temp2 = key1[i]
        key1[i] = key1[(ord(key2[i])-ord('a'))%14] 
        key1[(ord(key2[i])-ord('a'))%14] = temp2
        
        
    for i in range(14,28):
        temp1 = flag[i]
        flag[i] = flag[(ord(key2[i-14])-ord('a'))%28] 
        flag[(ord(key2[i-14])-ord('a'))%28] = temp1
        temp2 = key2[i-14]
        key2[i-14] = key2[(ord(key1[i-14])-ord('a'))%14] 
        key2[(ord(key1[i-14])-ord('a'))%14] = temp2
        

l = random.sample([key1, key2], 2)
key1 = l[0]
key2 = l[1]

k = ''
for i in range(14):
    k += random.choice(map)
k = list(k)

key2 = k+key2
for i in range(14):
    a = ord(k[i])-ord('a')+ord(key2[i+14])
    if a>122:
        a=a%122
        a=a+97
    key2[i+14]= chr(a)

flag = ''.join(flag)
key1 = ''.join(key1)
key2 = ''.join(key2)
 
key2 = enc2(key2)
flag= enc1(enc1(enc1(enc2(flag))))

print('Encrytped key1 = '+key1)
print('Encrypted key2 = '+key2)
print('Encrypted flag = '+flag)