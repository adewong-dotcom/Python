from paddle import Paddle
from ball import Ball

class AI():
    def __init__(self, ball, paddle):
        self.ball = ball
        self.paddle = paddle
        self.detect_movement()

    def detect_movement(self):
        # if self.paddle.distance(self.ball) <=450:
        ball_location = self.ball.ycor()

        paddle_location = self.paddle.ycor()
        if ball_location > 0:
            if paddle_location <= 0:
                self.paddle.up()
        elif ball_location == 0:
            if paddle_location > 0:
                self.paddle.down()
            elif paddle_location < 0:
                self.paddle.up()
        elif ball_location < 0:
            if paddle_location >=0:
                self.paddle.down()