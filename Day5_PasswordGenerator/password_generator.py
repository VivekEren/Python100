import string
import random

alpha = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the Python Password Generator")

pass_len = int(input("How long password you want?\n"))
pass_numbers = int(input("How many numbers you need in password?\n"))
pass_symbols = int(input("How many symbols you need in password?\n"))
pass_alpha = pass_len - (pass_numbers + pass_symbols)

pass_list = []

for i in range(pass_numbers):
    pass_list.append(numbers[random.randint(0, len(numbers)-1)])
    
for i in range(pass_symbols):
    pass_list.append(symbols[random.randint(0, len(symbols)-1)])

for i in range(pass_alpha):
    pass_list.append(alpha[random.randint(0, len(alpha)-1)])
    
password = ''

for i in range(len(pass_list)):
    password += pass_list.pop(random.randint(0, len(pass_list)-1))
    
print(f"Your password is {password}")





