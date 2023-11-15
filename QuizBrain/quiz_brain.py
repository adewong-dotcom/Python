class QuizBrain:
    def __init__(self, questions_list):
        self.question = 0
        self.questions_list = questions_list

    # TODO 1: asking the questions
    def next_question(self):
        user_answer = (input(f" Q.{self.question +1}: {self.questions_list[self.question].question} (True/False)?  ")
                       .capitalize())
        if user_answer == 'True' or user_answer == 'False':
            return user_answer
        print("That is not a valid answer.")

    # TODO 2: checking if the answer was correct
    def check_answer(self, user_answer):
        if self.questions_list[self.question].answer == user_answer:
            self.question += 1
            return True
        return False

    # TODO 3: checking if we're the end of the quiz
    def is_end(self):
        if self.question >= len(self.questions_list):
            return True
        return False
