import random
from hangman_art import stages, logo #calls the hangman_art.py and the graphics in them
from hangman_words import words_2nd_list, words_3rd_list, words_4th_list #gets the list of vocab words

print(logo)
print("Welcome to hangman")

#Recursive function that creates blank marks for each letter in word
def blank_maker(length):
	if length == 1:
		return "_"
	return "_" + blank_maker(length-1)


stages = stages
playing = True
while playing:
	#Reminder that /n in a string is used for new line and int is for type casting
	choose_level = int(input("What grade level would you like the vocabulary to be?\nType 2 for 2nd grade, 3 for 3rd grade, 4 for 4th grade or 0 to quit\n"))
	random_word = ""

	if choose_level == 0:
		playing = False
		break
	elif choose_level == 2:
		random_word = random.choice(words_2nd_list)
	elif choose_level == 3:
		random_word = random.choice(words_3rd_list)
	else:
		random_word = random.choice(words_4th_list)
	#creates blanks based on the number of letters in random word
	word_blank = blank_maker(len(random_word))
	print(word_blank)
	word_blank = [l for l in word_blank] #it creates a new List where each character is an item

	game_over = False
	current_guesses = "" # Keeps track of what the person has guessed up to now
	lives = 6

	while not game_over:
		print(stages[lives])
		guess = input("What is your guess? Add a single letter.\n")

		if len(guess) > 1 or !guess.isalpha(): #Checks is guess is more than one letter and not alpha
			print("Add a valid guess.")
			continue
		else:
			guess = guess.lower()
			if current_guesses.find(guess) >= 0: #if guess is in current guesses continue and let guess again
				print("You've already guessed that letter. Try a different letter.")
				continue
			else:
				current_guesses += guess #if not in current guesses add it current guesses

		if random_word.find(guess) < 0: # if less than 0 then it is -1 or not in word
			lives -= 1
			print("The letter is not in the word.")
			if lives == 0:
				print(stages[lives])
				print("You lose. Try again.")
				print(f"The word was: {random_word}") #Reveals the word end of game
				game_over = True
		else:
			for num in range(len(random_word)):
				if random_word[num] == guess:
					word_blank[num] = guess

		if "".join(word_blank) == random_word: #If the word matches then it has been discovered and the game has been won
			print("Great job! You win.\nLet's play again.")
			game_over = True

		print("".join(word_blank))


		
