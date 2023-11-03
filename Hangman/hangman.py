import random
from hangman_art import stages, logo
from hangman_words import words_2nd_list, words_3rd_list, words_4th_list

print(logo)
print("Welcome to hangman")


def blank_maker(length):
	if length == 1:
		return "_"
	return "_" + blank_maker(length-1)


stages = stages
playing = True
while playing:
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

	word_blank = blank_maker(len(random_word))
	print(word_blank)
	word_blank = [l for l in word_blank]

	game_over = False
	current_guesses = ""
	lives = 6

	while not game_over:
		print(stages[lives])
		guess = input("What is your guess? Add a single letter.\n")

		if len(guess) > 1:
			print("Add a valid guess.")
			continue
		else:
			guess = guess.lower()
			if current_guesses.find(guess) > 0:
				print("You've already guessed that letter. Try a different letter.")
				continue
			else:
				current_guesses += guess

		if random_word.find(guess) < 0:
			lives -= 1
			print("The letter is not in the word.")
			if lives == 0:
				print(stages[lives])
				print("You lose. Try again.")
				print(f"The word was: {random_word}")
				game_over = True
		else:
			for num in range(len(random_word)):
				if random_word[num] == guess:
					word_blank[num] = guess

		if "".join(word_blank) == random_word:
			print("Great job! You win.\nLet's play again.")
			game_over = True

		print("".join(word_blank))


		