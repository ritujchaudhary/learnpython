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

password = ""

for l in range(0,4):
    letter_index = random.randint(0,len(letters)-1)
    password = password + letters[letter_index]

for s in range(0,2):
  symbol_index = random.randint(0,len(symbols)-1)
  password = password + symbols[symbol_index]
                               
for n in range(0,2):
  number_index = random.randint(0,len(numbers)-1)
  password = password + numbers[number_index]
                              
print(f'easy way passwod: {password}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password2 = []

##choosing randomly method#1
for l in range(0,nr_letters):
  letter_index = random.randint(0,len(letters)-1)
  password2.append(letters[letter_index])

##choosing randomly method#2
for s in range(0,nr_symbols):
  symbol_pick = random.choice(symbols)
  password2.append(symbol_pick)
                               
##choosing randomly method#3
for n in range(0,nr_numbers):
  password2.append(random.choice(numbers))

print(password2)
random.shuffle(password2)
print(password2)
##print list to str

pass2 = ''

for char in password2:
    pass2 +=char

print(f'hard way passwod: {pass2}')
