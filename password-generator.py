import random

print("Welcome to the PyPassword Generator!")
password = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '@', '$', '%', '&', '(', ')', '*', '<', '>', '.', ',', '[', ']', '{', '}']
num_digits = int(input("How many digits would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_letters = num_digits-num_symbols-num_numbers

for n in range(num_digits):
	rand_digit = random.randint(0,2)
	if rand_digit == 0 and num_letters > 0:
		rand_case = random.randint(0, 1)
		rand_letter = random.choice(letters)
		if rand_case == 0:
			password += rand_letter
			num_letters -= 1
		else:
			password += rand_letter.upper()
			num_letters -= 1
	elif rand_digit == 1 and num_symbols > 0:
		rand_symbol = random.choice(symbols)
		password += rand_symbol
		num_symbols -= 1
	elif rand_digit == 2 and num_numbers > 0:
		rand_number = random.randint(0,9)
		password += str(rand_number)
		num_numbers -= 1
	elif rand_digit == 2 and num_numbers == 0:
		if num_letters > 0:
			rand_case = random.randint(0, 1)
			rand_letter = randon.choice(letters)
			if rand_case == 0:
				password += rand_letter
				num_letters -= 1
			else:
				password += rand_letter.upper()
				num_letters -= 1
		else:
			rand_symbol = symbols[random.randint(0, len(symbols)-1)]
			password += rand_symbol
			num_symbols -= 1
	elif rand_digit == 1 and num_symbols == 0:
		if num_letters > 0:
			rand_case = random.randint(0, 1)
			rand_letter = letters[random.randint(0, len(letters)-1)]
			if rand_case == 0:
				password += rand_letter
				num_letters -= 1
			else:
				password += rand_letter.upper()
				num_letters -= 1
		else:
			rand_number = random.randint(0,9)
			password += str(rand_number)
			num_numbers -= 1
	else:
		if num_numbers > 0:
			rand_number = random.randint(0,9)
			password += str(rand_number)
			num_numbers -= 1
		else:
			rand_symbol = symbols[random.randint(0, len(symbols)-1)]
			password += rand_symbol
			num_symbols -= 1

print(f"Your password is: {password}")
