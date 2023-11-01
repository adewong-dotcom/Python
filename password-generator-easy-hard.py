#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
nr_digits = nr_letters + nr_symbols + nr_numbers
temp_nr_letters = 0
temp_nr_symbols = 0
temp_nr_numbers = 0
password_easy = []
for n in range(0, nr_digits):
    if temp_nr_letters != nr_letters:
        password_easy.append(random.choice(letters))
        temp_nr_letters += 1
    elif temp_nr_symbols != nr_symbols:
        password_easy.append(random.choice(symbols))
        temp_nr_symbols += 1
    else:
        password_easy.append(random.choice(numbers))
        temp_nr_numbers += 1
easy_password_string = "".join(password_easy)
print(f"Your easy password is: {easy_password_string}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = []
for num in range(0, nr_digits):
    if nr_letters > 0 and nr_numbers > 0 and nr_symbols > 0:
        rand_digit = random.choice([letters, symbols, numbers])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isalpha():
            nr_letters -= 1
        elif rand_value.isnumeric():
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_letters > 0 and nr_numbers > 0:
        rand_digit = random.choice([letters, numbers])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isalpha():
            nr_letters -= 1
        else:
            nr_numbers -= 1
    elif nr_letters > 0 and nr_symbols > 0:
        rand_digit = random.choice([letters, symbols])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isalpha():
            nr_letters -= 1
        else:
            nr_symbols -= 1
    elif nr_numbers > 0 and nr_symbols > 0:
        rand_digit = random.choice([numbers, symbols])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isnumeric():
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_numbers > 0:
        rand_value = random.choice(numbers)
        password_hard.append(rand_value)
        nr_numbers -= 1
    elif nr_letters > 0:
        rand_value = random.choice(letters)
        password_hard.append(rand_value)
        nr_letters -= 1
    else:
        rand_value = random.choice(symbols)
        password_hard.append(rand_value)
        nr_symbols -= 1

print(f"Your hard password is: {''.join(password_hard)}")
print("Thank you for using the PyPassword Generator!")
