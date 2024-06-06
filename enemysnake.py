from snake import Snake
import random
from globals import Y_AXIS, X_AXIS


class EnemySnake(Snake):
    def __init__(self, length: int):
        hlp = 0
        super().__init__(length)
        self.function_tuple = (self.right, self.left, self.up, self.down)
        for segment in self.segments:
            segment.color("red")
            segment.goto(-X_AXIS + 20 + hlp, -Y_AXIS + 20)
            hlp -= 20

    def die(self, length: int) -> None:
        hlp = 0
        for i in range(len(self.segments) - 1, -1, -1):
            self.segments[i].hideturtle()
            self.segments[i].goto(-4000, -4000)
            self.segments.pop(i)
            
        super().__init__(length)
        self.function_tuple = (self.right, self.left, self.up, self.down)
        for segment in self.segments:
            segment.color("red")
            segment.goto(-X_AXIS + 20 + hlp, -Y_AXIS + 20)
            hlp -= 20

    def random_move(self):
        random.choice(self.function_tuple)()
