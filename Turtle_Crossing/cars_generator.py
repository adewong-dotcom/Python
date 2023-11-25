from turtle import Turtle
import random
import time

LEFT_BORDER = -400
RIGHT_BORDER = 400
TRAFFIC_SPACE = 63.75
TOP_BORDER = 280 - 31.875
BOTTOM_BORDER = -280 + 32.875
COLORS = ["#000000", "#0000FF", "#AFEEEE", "#F0E68C", "#FFD700", "#FF0000", "#4B0082"]
SIZES = [(4, 2), (4, 2)]
NUM_CARS = 5

class CarsGenerator():
    def __init__(self):
        self.traffic = []
        self.initialpositions = []
        self.level = 1
        self.lanes = self.lane_creator()

    def lane_creator(self):
        lanes = []
        top_lane_x = LEFT_BORDER
        top_lane_y = TOP_BORDER
        bottom_lane_x = RIGHT_BORDER
        bottom_lane_y = BOTTOM_BORDER
        

        for n in range(4):
            lanes.append((top_lane_x, top_lane_y))
            lanes.append((bottom_lane_x, bottom_lane_y))
            top_lane_y -= TRAFFIC_SPACE
            bottom_lane_y += TRAFFIC_SPACE

        return lanes

    def create_car(self):
        # for n in range(self.level * NUM_CARS):
        chance = random.randint(1, 6)
        if chance == 5:
            new_car = Turtle("square")
            color = random.choice(COLORS)
            new_car.color(color)
            size = random.choice(SIZES)
            new_car.shapesize(stretch_len=size[0], stretch_wid=size[1])
            new_car.pu()
            lane = random.choice(self.lanes)
            new_car.goto(lane)
            self.initialpositions.append(lane)
            self.traffic.append(new_car)
    
    def start_traffic(self):
        for n in range(len(self.traffic)):
            car = self.traffic[n]
            left = LEFT_BORDER + 20
            if self.initialpositions[n][0] <= LEFT_BORDER:
                car.forward(5)
            else:
                car.backward(5)

    def crash(self, player):
        for car in self.traffic:
            if car.distance(player) <= 40:
                return True
        return False

