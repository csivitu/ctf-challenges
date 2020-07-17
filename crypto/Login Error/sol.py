import binascii

def decode(num):
    hexstring=input()
    hexstring.encode('utf-8')
    enc=binascii.unhexlify(hexstring)
    ch=enc[6]
    if(num==1):
        xor=ord('?')^ord('s')
    else:
        xor=ord('?')^ord('t')
    ch=ch^xor
    ch=hex(ch)
    ch=ch[2:]
    ch=binascii.unhexlify(ch)
    enc=enc[:6]+ch+enc[7:]
    ans=binascii.hexlify(enc)
    print(str(ans)[2:-1])

decode(1)
decode(2)
