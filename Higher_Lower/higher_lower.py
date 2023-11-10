import random
from higher_lower_data import instagram_celebrities
from higher_lower_art import logo, vs
import os

score = 0

def clear():
	'''Clears the screen'''
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

#Function to print information about celebrity
def celebrity_info(name):
	'''Gets the name of the celebrity and returns a detailed explanation of what he/she/it does'''
	profession = instagram_celebrities[name]["Profession/Activity"]
	country = instagram_celebrities[name]["Country"]
	return f"{name} : {profession} from {country}."

#Function that compares celebrities
def is_winner(celebs):
	'''Gets a list of celebs and returns the one with the highest amount of followers as 'A' or 'B'''
	celeb1 = celebs[0]
	celeb2 = celebs[1]
	followers_celeb1 = instagram_celebrities[celeb1]["Followers"]
	followers_celeb2 = instagram_celebrities[celeb2]["Followers"]
	if followers_celeb1 > followers_celeb2:
		return 'A'
	return 'B'

#Function that randomly chooses a celebrity
def celeb_selector(current_celeb = None):
	'''Returns a random celebrity.
	Optionally gets the current celeb to prevent repeating.'''
	rand_celeb = random.choice(list(instagram_celebrities.keys()))
	if current_celeb == rand_celeb:
		return celeb_selector(current_celeb)
	else:
		return rand_celeb


def continue_game(score):
	'''Continues game with score'''
	print(f"You're right! Current score: {score}.")

def celeb_data():
	'''Chooses and prints celeb data, returns celebs as list'''
	celebs = []
	celebs.append(celeb_selector())
	celebs.append(celeb_selector(current_celeb = celebs[0]))

	celeb1_info = celebrity_info(celebs[0])
	celeb2_info = celebrity_info(celebs[1])

	print(f"Compare A: {celeb1_info}")
	print(vs)
	print(f"Against B: {celeb2_info}")
	return celebs


game_over = False
while not game_over:
	print(logo)
	if score > 0:
		continue_game(score)

	celebs = celeb_data()
	winner = is_winner(celebs)
	choosing = True

	while choosing:
		choice = input("Who has more followers? Type 'A' or 'B':  ").upper()
		if choice == winner:
			score += 1
			choosing = False
			clear()
		elif choice != winner:
			clear()
			print(logo)
			print(f"Sorry, that's wrong. Final score: {score}")
			game_over = True
			choosing = False
		else:
			print('That is not a valid response.')
