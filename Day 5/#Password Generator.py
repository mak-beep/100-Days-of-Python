import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','~']

print("Welcome to the Password Generators!!!")

nr_letters = int(input('How many letters would you like in your password? \n'))
nr_numbers = int(input('How many numbers would you like in your password? \n'))
nr_symbols = int(input('How many symbols would you like in your password? \n'))

# # Easy Level

# password = ''
# for i in range(0,nr_letters):
#     random_letter = random.choice(letters)
#     password += random_letter
# for i in range(0,nr_numbers):
#     random_number = random.choice(numbers)
#     password += random_number
# for i in range(0,nr_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol

# print(password)

# Hard Level

password_list = []
password = ''
for i in range(0,nr_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for i in range(0,nr_numbers):
    random_number = random.choice(numbers)
    password_list += random_number
for i in range(0,nr_symbols):
    random_symbol = random.choice(symbols)
    password_list += random_symbol

# print(password_list)
random.shuffle(password_list)

# Prints the list.

# print(password_list)

# To print the password as a string
for char in password_list:
    password += char

print(f"Your password is. {password}")