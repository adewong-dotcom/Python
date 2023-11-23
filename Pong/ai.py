from paddle import Paddle
from ball import Ball

class AI():
    def __init__(self, ball, paddle):
        self.ball = ball
        self.paddle = paddle
        self.detect_movement()

    def detect_movement(self):
        ball_location_y = self.ball.ycor()
        ball_location_x = self.ball.xcor()
        paddle_location = self.paddle.ycor()

        if ball_location_x <=450:
            if ball_location_y > paddle_location:
                self.paddle.up()
            elif ball_location_y < paddle_location:
                self.paddle.down()
            else:
                pass
        #delete this part to make is slightly slower
        else:
            if ball_location_y > paddle_location:
                self.paddle.down()
            elif ball_location_y < paddle_location:
                self.paddle.up()
            else:
                pass
