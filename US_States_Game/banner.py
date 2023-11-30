from turtle import Turtle
FONT = ("Arial, 40, normal")
ALIGNMENT = "center"

class Banner(Turtle):
    def __init__(self, score):
        super.__init__()
        self.score = score
    
    def game_over(self):
        if self.score == 50:
            self.write(arg="You know your states!", font=FONT, align=ALIGNMENT)
        else:
            self.write(arg=f"You got {self.score} of the states!", font=FONT, align=ALIGNMENT)