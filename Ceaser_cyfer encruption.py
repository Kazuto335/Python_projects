alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()


def encrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encoded_text = ""
    for a in text:
        if a in alphabet:
            encoded_text += alphabet[alphabet.index(a) + shift] 
        else:
            encoded_text += a
    print(encoded_text)
    
def decrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decoded_text = ""
    for a in text:
        if a in alphabet:
            decoded_text += alphabet[alphabet.index(a) - shift] 
        else :
            decoded_text += a
    print(decoded_text)

if direction == "encode":
    encrypt()
elif direction == "decode":
    decrypt()
else: 
    print("Wrong input..!")
