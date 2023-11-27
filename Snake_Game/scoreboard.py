from turtle import Turtle

SCREENWIDTH = 300
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = self.get_highscore()
        location = "Snake_Game/high_score.txt"
        with open(location) as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.pu()
        y_position = SCREENWIDTH - 30
        self.setposition(x=-20, y=y_position)
        self.color('white')
        self.draw_board()
    
    def update_score(self):
        self.score += 1
        self.draw_board()
    
    def draw_board(self):
        self.clear()
        self.write(arg= f"Score: {self.score}  High Score: {self.high_score}", align = ALIGNMENT, font= FONT)
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg= "GAME OVER", align = ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_highscore()
        self.score = 0
        self.draw_board()

    def get_highscore(self):
        location = "Snake_Game/high_score.txt"
        with open(location) as file:
            int(file.read())

    def set_highscore(self):
        location = "Snake_Game/high_score.txt"
        with open(location, mode= "w") as file:
            file.write(f"{self.high_score}")