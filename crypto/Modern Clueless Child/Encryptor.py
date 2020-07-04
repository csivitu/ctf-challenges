#EncryptingWithXOR

input_str = raw_input("Enter the cipher text : ")
key = raw_input("Enter the key for xor-ing : ")
output_str = ""
no_of_itr=len(input_str)


for i in range(no_of_itr):
    current = input_str[i]
    current_key = key[i%len(key)]
    output_str += chr(ord(current) ^ ord(current_key))

final_str=""
for character in output_str:
    final_str+= character.encode('hex')
print final_str