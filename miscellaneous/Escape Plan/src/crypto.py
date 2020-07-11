def shift_cipher_key(text, s):
    print(chr(27) + "[2j")
    print("\033c")
    print("\x1bc")
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print(f"The text '{text}' with shift {s} is '{result}'")


def shift_cipher_bruteforce(text):
    print(chr(27) + "[2j")
    print("\033c")
    print("\x1bc")
    for s in range(1, 26):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        print(f"The text '{text}' with shift {s} is '{result}'")


def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    print(chr(27) + "[2j")
    print("\033c")
    print("\x1bc")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ""
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    print(f"ciphertext: {ciphertext}")


def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    print(chr(27) + "[2j")
    print("\033c")
    print("\x1bc")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ""
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    print(f"plaintext: {plaintext}")


while True:
    print(
        """

Welcome to cipher decoder, an open-source script in python!

EXAMPLES:
    shift_cipher_key('hello', 25)
    shift_cipher_bruteforce('hello')
    encrypt_vigenere('TEXT', 'KEY')
    decrypt_vigenere('DIVD', 'KEY')

Currently supported ciphers:
    shift_cipher_key(text, shift)
    shift_cipher_bruteforce(text)
    encrypt_vigenere(plaintext, key)
    decrypt_vigenere(ciphertext, key)

To exit:
    exit()

I am constantly trying to make this cipher decoder better and more secure! Help me add support to more ciphers by submitting a PR!
Hope it helps you!

    """
    )
    try:
        eval(input())
    except BaseException as e:
        if str(type(e)) == "<class 'SystemExit'>":
            print("Thank you for using cipher decoder!")
            break
        else:
            print("Something went wrong!")

