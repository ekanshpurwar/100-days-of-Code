alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
def encrypt(text, shift):
    list_letter = list(text)
    encrypt_text = ""
    shift = shift % 26
    for i in list_letter:
        if i in alphabet:

            index_letter = alphabet.index(i)
            new_index = index_letter + shift
            if new_index > 25:
                new_index = (new_index - index_letter) - shift
            encrypt_text += alphabet[new_index]
        else:
            encrypt_text+=i
    print("The encoded text is ", encrypt_text)


def decrypt(text, shift):
    list_letter = list(text)
    decrypt_text = ""
    shift = shift % 26
    for i in list_letter:
        if i in alphabet:
            index_letter = alphabet.index(i)
            new_index = index_letter - shift
            decrypt_text += alphabet[new_index]
        else:
            decrypt_text+=i
    print("The decoded text is ", decrypt_text)

print(logo)

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
        continue
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
        continue
    else:
        exit(-1)