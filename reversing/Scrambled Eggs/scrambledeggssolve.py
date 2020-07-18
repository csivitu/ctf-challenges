
map = ['v', 'r', 't', 'p', 'w', 'g', 'n', 'c', 'o', 'b', 'a', 'f', 'm', 'i', 'l', 'u', 'h', 'z', 'd', 'q', 'j', 'y', 'x', 'e', 'k', 's']

cflag = 'qotiwvrcqndlvvrafwgtocdrdzfd'
cflag = list(cflag)

ckey = 'eudlqgluduggdluqmocgyukhbqkx'
ckey = list(ckey)
k=''
ckey2 = ''
ckey1 = ''

def decrypt2(text):
    for i in range(len(text)):
        a = map.index(text[i])
        c = chr(ord('a')+a)
        text[i] = c
    return text
        
        
        
cflag = decrypt2(cflag)
cflag = ''.join(cflag)        
ckey = decrypt2(ckey)        


cflag = list(cflag)

for i in range(14,28):
    a = (ord(ckey[i])-(ord(ckey[i-14])-ord('a')))
    if 97>a:
        a = 97-a
        a = 122-a
    ckey[i] = chr(a)
    ckey1 += ckey[i]
    
ckey2 = 'xtfsyhhlizoiyx'

ckey1 = list(ckey1)
ckey2 = list(ckey2)

#ckey1 = 'rettnahagbeogi'
#ckey2 = 'xtfsyhhlizoiyx'
#could be interchangeable 

for j in range(2):
 for i in range(27,13,-1):
    temp = ckey2[i-14]
    ckey2[i-14] = ckey2[(ord(ckey1[i-14])-ord('a'))%14]
    ckey2[(ord(ckey1[i-14])-ord('a'))%14] = temp 
    temp1 = cflag[i]
    cflag[i] = cflag[(ord(ckey2[i-14])-ord('a'))%28] 
    cflag[(ord(ckey2[i-14])-ord('a'))%28] = temp1
  
 for i in range(13,-1,-1):
    temp2 = ckey1[i]
    ckey1[i] = ckey1[(ord(ckey2[i])-ord('a'))%14] 
    ckey1[(ord(ckey2[i])-ord('a'))%14] = temp2
    temp1 = cflag[i]
    cflag[i] = cflag[(ord(ckey1[i])-ord('a'))%28] 
    cflag[(ord(ckey1[i])-ord('a'))%28] = temp1
        

b = decrypt2(decrypt2(ckey2))
if ckey1 == b:
    print('YAAAAAAAAAY')
    
print(cflag)


        
