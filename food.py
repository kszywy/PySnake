from globals import Y_AXIS, X_AXIS, COLORS
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(0.8, 0.8)
        self.speed(0)
        self.change_location()

    def is_eaten(self, turtle: Turtle) -> bool:
        if self.distance(turtle) <= 20:
            return True
        return False

    def change_location(self) -> None:
        self.goto(random.randint(-X_AXIS + 30, X_AXIS - 30),
                  random.randint(-Y_AXIS + 30, Y_AXIS - 30))
        self.color(random.choice(COLORS))


class FakeFood(Food):
    def __init__(self):
        super().__init__()
        self.color("red")

    def change_location(self):
        self.goto(random.randint(-X_AXIS + 20, X_AXIS - 20),
                  random.randint(-Y_AXIS + 20, Y_AXIS - 20))
