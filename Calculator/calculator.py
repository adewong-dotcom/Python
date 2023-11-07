import math
from calculator_art import logo, brand
from sys import float_info
from functools import reduce

# statement_operations = ['{','}','[',']','(',')']
prime_numbers = "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293"
prime_numbers = prime_numbers.split(", ")

def is_float(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def get_list():
	returned_list = []
	getting_input = True
	while getting_input:
		if len(returned_list) < 1:
			number = input("Enter the first number:  ")
			if number == '0':
				getting_input = False
				break
			elif is_float(number) and number != '0':
				returned_list.append(int(number))
			else:
				print("That is not a valid number. Try again.")
				continue
		else:
			number = input("Enter the next number or 0 to get result:  ")
			if number == '0':
				getting_input = False
				break
			elif is_float(number) and number != '0':
				returned_list.append(int(number))
			else:
				print("That is not a valid number. Try again.")
				continue
	return returned_list

def euclidGCD(a, b):
	if b==0:
		return a
	primeA = a%b
	return euclidGCD(b, primeA)


def gcd():
	"""Gets list input from user and returns gcd. Doesn't require any parameters."""
	list_numbers = get_list()
	answer = reduce(lambda x,y: euclidGCD(x,y), list_numbers)
	return answer
def lcm():
	list_numbers = get_list()
	l = reduce(lambda x, y: math.lcm(x, y), list_numbers)
	return l

def addition(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1/num2

operations = {
	"+": addition, 
	"-": subtract, 
	"*": multiply, 
	"/": divide
	}
extra_operations = {
	'gcd': gcd, 
	'lcm': lcm
	}
print(logo)
print(brand)
calculator_working = True
while calculator_working:
	print("You can choose to do a simple operation with two numbers, such as \naddition, subtraction, multiplication or division, or get the GCD \nor LCM from a list.")
	print("Type 'simple' to do a simple operation\nType 'gcd' to obtain the GCD of a list of numbers\nType 'lcm' to get the LCM of a list of numbers")
	print("Type '0' to exit.")
	type_operation = input()

	if type_operation == 'simple':
		getting_input = True
		while getting_input:
			num1 = input("What's the first number?:  ")
			if is_float(num1):
				num1 = float(num1)
				getting_input = False
			else:
				print("That is not a valid value.")
				continue
		for symbol in operations:
			print(symbol)
		operation_symbol = input("Pick an operation from the line above:  ")

		getting_input = True
		while getting_input:
			num2 = input("What's the second number?:  ")
			if is_float(num2):
				num2 = float(num2)
				getting_input = False
			else:
				print("That is not a valid value.")
				continue

		operation = operations.get(operation_symbol)
		print("The result is: ", operation(num1, num2))
		print()
	elif type_operation == 'gcd' or type_operation == 'lcm':
		operation = extra_operations.get(type_operation)
		print(f"The {type_operation} is: ",operation())
		print()
	elif type_operation == '0':
		calculator_working = False
		print("Thanks for using the Pythonista calculator!")
	else:
		print("That is not a valid option.")
		print()


