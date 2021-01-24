# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# selecting random letter
str_letter = ""
for i in range(nr_letters):
    str_letter += random.choice(letters)

# selecting random symbol
str_symbol = ""
for i in range(nr_symbols):
    str_symbol += random.choice(symbols)

# selecting random number
str_number = ""
for i in range(nr_numbers):
    str_number += random.choice(numbers)
str_password = str_letter + str_symbol + str_number
print(str_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_password = []
random_order_password = ""
for i in str_password:
    list_password += i
length_list=len(list_password)
for j in range(length_list):

    random_order_password += random.choice(list_password)

    # Removing the repetion of letter in final password
    for k in random_order_password:
        if k in list_password:
            list_password.remove(k)
        else:
            continue

print(random_order_password)

