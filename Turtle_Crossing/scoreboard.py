from turtle import Turtle

PLACEMENT = (-375, 303)
FONT = ("Courier", 30, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.pu()
        self.color("#000000", "#FFFFFF")
        self.goto(PLACEMENT)
        self.draw_board()
    
    def draw_board(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        
    def update(self):
        self.level += 1
        self.clear()
        self.draw_board()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)