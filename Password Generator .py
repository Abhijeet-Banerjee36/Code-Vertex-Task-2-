# py password generator 
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
len_letters=len(letters)
len_numbers=len(numbers)
len_symbols=len(symbols)
easy_letters=''
for i in range(1,nr_letters+1):
    random_letter_index=random.randint(0,len_letters-1)
    easy_letters+=str(letters[random_letter_index])

easy_numbers=''
for j in range(1,nr_numbers+1):
    random_number_index=random.randint(0,len_numbers-1)
    easy_numbers+=str(numbers[random_number_index])

    
easy_symbols=''
for k in range(1,nr_symbols+1):
    random_symbol_index=random.randint(0,len_symbols-1)
    easy_symbols+=str(symbols[random_symbol_index])


easy_total_password=easy_letters+easy_symbols+easy_numbers
print(easy_total_password)

'''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

'''password_list=[]

for char in range(1,nr_letters+1):
    password_list += random.choice(letters)

for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password=''
for char in password_list:
    password+=char

print(f"Your password is {password}")
'''