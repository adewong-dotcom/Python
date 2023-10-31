rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

upset_face = '''
             /
    --     --
   (  )   (  )
    --     --
        ()

      -------
  '''

user_choice = int(
    input("Choose one. Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
answer_rand = random.randint(0, 3)
praises = [
    "You win.", "You won! What a match!", "You win...this round.",
    "You are really good at this...I want a rematch!"
]
losses = [
    "You lose.", "Woohoo!..I mean better luck next time.", "I won!",
    "Woohoo! I won!"
]
draws = [
    "It's a draw.", "It's a tie.", "You read my mind!",
    "Hmmm...let's try that again."
]

hands = [rock, paper, scissors]
if (user_choice >= len(hands) or user_choice < 0):
    print(upset_face)
else:
    print(hands[user_choice] + "\n")
    print("Computer chose:\n")
    print(hands[computer_choice] + "\n")

if user_choice == computer_choice:
    print(draws[answer_rand])
elif user_choice == 0:
    if computer_choice == 1:
        print(losses[answer_rand])
    else:
        print(praises[answer_rand])
elif user_choice == 1:
    if computer_choice == 0:
        print(praises[answer_rand])
    else:
        print(losses[answer_rand])
elif user_choice == 2:
    if computer_choice == 0:
        print(losses[answer_rand])
    else:
        print(praises[answer_rand])
else:
    print("That is not a valid response. Try again.")
