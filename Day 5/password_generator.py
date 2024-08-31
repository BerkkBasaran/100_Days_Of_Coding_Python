import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like your password?\n"))
number_of_symbols = int(input("How many symbols would you like? \n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

loop_letters = 0
loop_symbols = 0
loop_numbers = 0

for letter in letters:
    if loop_letters <= number_of_letters:
        password.append(random.choice(letters))
    loop_letters += 1
for symbol in symbols:
    if loop_symbols <= number_of_symbols:
        password.append(random.choice(symbols))
    loop_symbols += 1
for number in numbers:
    if loop_numbers <= number_of_numbers:
        password.append(random.choice(numbers))
    loop_numbers += 1    

random.shuffle(password)
print("".join(password))