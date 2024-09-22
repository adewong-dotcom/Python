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
password_easy = [] #List to save characters of password
#Generates password first for letters, then symbols then numbers
for n in range(0, nr_digits):
    if temp_nr_letters != nr_letters:
        #adds character to end of list
        password_easy.append(random.choice(letters))
        temp_nr_letters += 1
    elif temp_nr_symbols != nr_symbols:
        password_easy.append(random.choice(symbols))
        temp_nr_symbols += 1
    else:
        password_easy.append(random.choice(numbers))
        temp_nr_numbers += 1
#Joins all of the characters in the list to a string and empty string joins it with nothing in between
easy_password_string = "".join(password_easy)
print(f"Your easy password is: {easy_password_string}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = [] #List with characters for password
for num in range(0, nr_digits):
    if nr_letters > 0 and nr_numbers > 0 and nr_symbols > 0: #if all three are greater than 0
        rand_digit = random.choice([letters, symbols, numbers]) #choose randomly from one of the three List of values
        rand_value = random.choice(rand_digit) #choose a value from the chosen List
        password_hard.append(rand_value)#add value to List password_hard
        if rand_value.isalpha(): #if it's alpha then letter was chosen and it should be lowered by 1
            nr_letters -= 1
        elif rand_value.isnumeric(): #if it's numeric then a number was chosen and it should be lowered by 1
            nr_numbers -= 1
        else: #if it's not alpha nor numeric, it must be a symbol and lower by 1
            nr_symbols -= 1
    elif nr_letters > 0 and nr_numbers > 0: #if first is false but this is true it's because we only have letters and numbers left
        rand_digit = random.choice([letters, numbers])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isalpha():
            nr_letters -= 1
        else:
            nr_numbers -= 1
    elif nr_letters > 0 and nr_symbols > 0: #otherwise only letters and symbols are left
        rand_digit = random.choice([letters, symbols])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isalpha():
            nr_letters -= 1
        else:
            nr_symbols -= 1
    elif nr_numbers > 0 and nr_symbols > 0: #or only numbers and symbols
        rand_digit = random.choice([numbers, symbols])
        rand_value = random.choice(rand_digit)
        password_hard.append(rand_value)
        if rand_value.isnumeric():
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_numbers > 0: #if the previous are false, we only have one set of values left which can be numbers
        rand_value = random.choice(numbers)
        password_hard.append(rand_value)
        nr_numbers -= 1
    elif nr_letters > 0: #or letters
        rand_value = random.choice(letters)
        password_hard.append(rand_value)
        nr_letters -= 1
    else: #or symbols
        rand_value = random.choice(symbols)
        password_hard.append(rand_value)
        nr_symbols -= 1
#We use an f string to add the method that transforms the list into a string directly in the print statement
print(f"Your hard password is: {''.join(password_hard)}")
print("Thank you for using the PyPassword Generator!")
