encryptedKey = 'ieluvnvfgvfahuxhvfphbppnbgrfcrn'
encryptedText = '»·­ª»£µ±¬¥¼±ºµ±¿·£¦­´¯ª¨¥«¥¦«´¸¦¡¸¢²§¤¦¦¹¨'

def dec4(text):
    mapping = [23, 9, 5, 6, 22, 28, 25, 30, 15, 8, 16, 19, 24, 11, 10, 7, 2, 14, 18, 1, 29, 21, 12, 4, 20, 0, 26, 13, 17, 3, 27]

    temp = [None]*len(text)

    for i in range(len(text)):
        temp[mapping[i]] = text[i]
    
    return ''.join(temp)

# If you notice, enc1 is actually a Caesar's cipher.
# You can bruteforce all values of 'r' to get all possible keys.
def dec1(text):
    return '\n'.join([bytes.fromhex(''.join([hex(((ord(i) - ord('a') - r) % 26) + ord('a'))[2:] for i in text])).decode('ascii') for r in range(26)])

# This is a list of all possible keys
keyList = dec4(dec4(encryptedKey))

# This is the key list:
# vafbivrgehffvncvxnpuhpngpurflbh
# uzeahuqfdgeeumbuwmotgomfotqekag
# tydzgtpecfddtlatvlnsfnlenspdjzf
# sxcyfsodbeccskzsukmremkdmrociye
# rwbxerncadbbrjyrtjlqdljclqnbhxd
# qvawdqmbzcaaqixqsikpckibkpmagwc
# puzvcplaybzzphwprhjobjhajolzfvb
# otyubokzxayyogvoqginaigzinkyeua
# nsxtanjywzxxnfunpfhmzhfyhmjxdtz
# mrwszmixvywwmetmoeglygexgliwcsy
# lqvrylhwuxvvldslndfkxfdwfkhvbrx
# kpuqxkgvtwuukcrkmcejwecvejguaqw
# jotpwjfusvttjbqjlbdivdbudiftzpv
# insovietrussiapikachucatchesyou
# hmrnuhdsqtrrhzohjzbgtbzsbgdrxnt
# glqmtgcrpsqqgyngiyafsayrafcqwms
# fkplsfbqorppfxmfhxzerzxqzebpvlr
# ejokreapnqooewlegwydqywpydaoukq
# dinjqdzompnndvkdfvxcpxvoxczntjp
# chmipcynlommcujceuwbowunwbymsio
# bglhobxmknllbtibdtvanvtmvaxlrhn
# afkgnawljmkkashacsuzmusluzwkqgm
# zejfmzvkiljjzrgzbrtyltrktyvjpfl
# ydielyujhkiiyqfyaqsxksqjsxuioek
# xchdkxtigjhhxpexzprwjrpirwthndj
# wbgcjwshfiggwodwyoqviqohqvsgmci

# In this list, you can see that there's a key in English
# insovietrussiapikachucatchesyou

# Even if you don't get this, you can bruteforce this later.

key = 'insovietrussiapikachucatchesyou'

def dec3(text):
    mapping = [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

# This is the XOR cipher, hence the same function can be used to decrypt it.
# Notice that we already know the key here, if not, we could bruteforce for all values of the key.
def dec2(text, key):
    k = [key[i % len(key)] for i in range(len(text))]
    return ''.join([chr(ord(text[i]) ^ ord(k[i]) + ord('a')) for i in range(len(text))])

message = dec1(dec2(dec3(dec3(encryptedText)), key))

print(message)