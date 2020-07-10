# solution to cipher one :

# after converting to python code:
def substitution_cipher(text):
    ret_text=""
    for i in list(text):
        ret_text += chr(2*ord(i)-len(text))
    return ret_text

#reversing :
def reverse_substitution_cipher(text):
    ret_text=""
    for i in list(text):
        ret_text += chr((ord(i)+len(text))//2)
    return ret_text

# solution to cipher two :

# after converting to python code:

def XOR(inpString): 
    xorKey = 'S'
    length = len(inpString)
    for i in range(length):
        inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i + 1:]) 
         
      
    return inpString

# reversing(as the following function is XOR its reverse is itself) :
