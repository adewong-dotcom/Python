import random
from guess_number_art import logo

print(logo)
print("Welcome to Guess the Number.")
running = True

while running:

	rand_num = random.randint(1,100)
	level = input("Choose a level. Type 'easy' for the easy level or 'hard' for the hard level.\n")
	tries = 0
	if level == 'easy':
		tries = 10
	elif level == 'hard':
		tries = 5
	else:
		print("That is not a valid input.")
		continue
	guesses = []

	while tries > 0:
		guess = input("Guess a number from 1 to 100.\n")

		try:
			guess = int(guess)
		except ValueError:
			print("That is not a valid input.\n")
			continue

		if guess == rand_num:
			print(f"You win the number was {guess}.")
			tries = 0
		elif guess in guesses:
			print(f"You already guessed {guess}. Try again.")
			continue
		elif guess > rand_num:
			guesses.append(guess)
			tries -= 1
			print(f"Less than {guess}")
		else:
			guesses.append(guess)
			tries -= 1
			print(f"Greater than {guess}")

	getting_input = True
	
	while getting_input:		
		play_again = input("Would you like to play again?\n Type 'y' for yes or 'n' for no.\n")

		if play_again == 'y':
			getting_input = False
		elif play_again == 'n':
			getting_input = False
			running = False
			print("Thanks for playing Guess the Number.")
		else:
			print("That is not a valid input.")

