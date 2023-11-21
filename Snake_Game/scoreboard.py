from turtle import Turtle

SCREENWIDTH = 300
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        y_position = SCREENWIDTH - 30
        self.setposition(x=-20, y=y_position)
        self.color('white')
        self.draw_board()
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.draw_board()
    
    def draw_board(self):
        self.write(arg= f"Score: {self.score}", align = ALIGNMENT, font= FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg= "GAME OVER", align = ALIGNMENT, font= FONT)