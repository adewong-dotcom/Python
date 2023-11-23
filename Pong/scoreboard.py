from turtle import Turtle

POSITIONS = ((-100, 250), (100, 250))
FONT = ("Consolas", 42, "normal")
ALIGNMENTS= ["left", "right"]

class Scoreboard(Turtle):
    def __init__(self):
        #self.scores is [player, computer]
        self.scores = [0, 0]
        self.scoreboard = []
        self.create_scoreboard()
        
    def create_scoreboard(self):
        for index in range(2):
            new_scoreboard = Turtle()
            new_scoreboard.pu()
            new_scoreboard.hideturtle()
            new_scoreboard.setposition(POSITIONS[index])
            new_scoreboard.color("#FFFFFF")
            new_scoreboard.write(arg=f"{self.scores[index]}", align = ALIGNMENTS[index], font=FONT)
            self.scoreboard.append(new_scoreboard)

    def update_scoreboard(self, user):
        if user == "player":
            index = 0
        else:
            index = 1
        current_scoreboard = self.scoreboard[index]
        current_scoreboard.clear()
        current_scoreboard.write(arg=f"{self.scores[index]}", align = ALIGNMENTS[index], font=FONT)
   
    def update_score(self, user):
        if user == "player":
            self.scores[0] += 1
        else:
            self.scores[1] += 1
        self.update_scoreboard(user)

    def get_score(self, user):
        if user == "player":
            return self.scores[0]
        return self.scores[1]
    
    def game_over(self, winner):
        new_scoreboard = Turtle()
        new_scoreboard.pu()
        new_scoreboard.hideturtle()
        new_scoreboard.color("#FFFFFF")
        if winner == "player":
            new_scoreboard.write(arg="Congratulations! You are a Python Pong master.", align = "center", font = FONT)
        else:
            new_scoreboard.write(arg="You lose.", align = "center", font = FONT)