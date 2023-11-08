import random
from black_jack_art import logo, cards_art

cards = {'A': 4, 'K': 4, 'Q': 4, 'J': 4, '10': 4, '9': 4, '8': 4, '7': 4, '6': 4, '5': 4, '4': 4, '3': 4, '2': 4}
values = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
card_types = "A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2"
card_types = card_types.split(", ")
shuffle_tracker = {'A': [], 'K': [], 'Q': [], 'J': [], '10': [], '9': [], '8': [], '7': [], '6': [], '5': [], '4': [], '3': [], '2': []}

def draw_card():
	rand_card = random.choice(card_types)
	if cards[rand_card] > 0:
		cards[rand_card] -= 1
		return rand_card
	else:
		draw_card()
def shuffle(card_type):
	'''
	Gets the card type to return a random suit which hasn't been
	chosen previously
	'''
	card_list = cards_art.get(card_type)
	rand_suit = random.choice(card_list)
	index_suit = card_list.index(rand_suit)
	if index_suit in shuffle_tracker[card_type]:
		return shuffle(card_type)
	else:
		shuffle_tracker[card_type].append(index_suit)
		return rand_suit

def reset_deck():
	cards = {'A': 4, 'K': 4, 'Q': 4, 'J': 4, '10': 4, '9': 4, '8': 4, '7': 4, '6': 4, '5': 4, '4': 4, '3': 4, '2': 4}
	shuffle_tracker = {'A': [], 'K': [], 'Q': [], 'J': [], '10': [], '9': [], '8': [], '7': [], '6': [], '5': [], '4': [], '3': [], '2': []}
print(logo)
playing = True


while playing:
	player_hand = []
	computer_hand = []
	player_cards = []
	computer_cards = []
	player_count = 0
	computer_count = 0

	for i in range(0,2):
		player_card = draw_card()
		player_cards.append(player_card)
		player_hand.append(shuffle(player_card))
		player_count += values.get(player_card)
		computer_card = draw_card()
		computer_cards.append(computer_card)
		computer_hand.append(shuffle(computer_card))
		computer_count += values.get(computer_card)

	print("Your hand is: ")
	for card in player_hand:
		print(card)
	print("Computer's hand is: ", computer_hand[0])
	print()

	if computer_count < 14:
		computer_card = draw_card()
		computer_cards.append(computer_card)
		computer_hand.append(shuffle(computer_card))
		computer_count += values.get(computer_card)

	getting_cards = True
	while getting_cards:
		another_card = input("Would you like another card?\n Type 'y' for yes or 'n' for no.\n").lower()
		if another_card == 'y':
			player_card = draw_card()
			player_cards.append(player_card)
			player_hand.append(shuffle(player_card))
			player_count += values.get(player_card)
			print("Your hand is: ")
			for card in player_hand:
				print(card)
			print("Computer's hand is: ", computer_hand[0])
			print()
			if player_count > 21 and 'A' not in player_hand:
				getting_cards = False
				break
		elif another_card == 'n':
			getting_cards = False
		else:
			print("That is not a valid input.")

	print("Your hand is: ")
	for card in player_hand:
		print(card)
	print("Computer's hand is: ")
	for card in computer_hand:
		print(card)
	print()
	if (player_count > computer_count and player_count<= 21) or (computer_count > 21 and player_count <= 21):
		print(f"You win with {player_count}.\n")
	elif player_count == computer_count:
		print(f"It's a draw. You both have {computer_count}. Try again.\n")
	else:
		print(f"You lose. You had {player_count} but the computer had {computer_count}.\n")
	while playing:	
		print("Do you want to play again?")
		play_again = input("Type 'y' for yes or 'n' for no.\n").lower()

		if play_again == 'n':
			playing = False
		elif play_again == 'y':
			reset_deck()
			break
		else:
			print("That is not a valid input.")

