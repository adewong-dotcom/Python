import os
from silent_auction_art import logo
import math

print(logo)
print("Welcome to the secret auction program.")

auction_in_progress = True
bidders = {}
# highest_bidder = ""

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def is_float(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

while auction_in_progress:
	bidder = input("What is your name?:  ")
	if not bidder.isalpha():
		print("That is not a valid input. Usernames are not allowed.")
		continue
	amount = input("What's your bid?:  $")
	if is_float(amount):
		amount = float(amount)
	else:
		print("That is not a valid input. Only include numbers.")
		continue


	# if len(bidders) == 0:
	# 	bidders[bidder] = amount
	# 	highest_bidder = bidder

	# elif amount > bidders[highest_bidder]:
	# 	bidders[bidder] = amount
	# 	highest_bidder = bidder
	# else:
	# 	bidders[bidder] = amount
	bidders[bidder] = amount

	ending_input = True
	while ending_input:
		continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
		if continue_bid == "yes" or continue_bid == "y":
			ending_input = False
			clear()
		elif continue_bid == "no" or continue_bid == "n":
			clear()
			auction_in_progress = False
			ending_input = False

			highest_bidder = ""
			highest_bid = 0

			for name in bidders:
				if bidders[name] > highest_bid:
					highest_bidder = name
					highest_bid = bidders[name]

			frac, whole = math.modf(highest_bid)
			highest_bid = str(highest_bid)
			frac *= 100
			second_decimal = frac%10
			if second_decimal == 0:
				highest_bid += '0'


			# print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}.")
			print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
		else:
			print("That is not a valid option.")