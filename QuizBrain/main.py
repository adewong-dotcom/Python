from question import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_art import logo

print(logo)
question_bank = []
for value in question_data:
    temp = Question(value["text"], value["answer"])
    question_bank.append(temp)

game = QuizBrain(question_bank)
running = True
while running:
    user_answer = game.next_question()
    if user_answer is None:
        continue
    correct = game.check_answer(user_answer)
    if game.is_end() or not correct:
        running = False
        if correct:
            print("Great job! You got them all correct.")
        else:
            print(f"You got {game.question} / {len(question_bank)}. Try again.")
        continue
