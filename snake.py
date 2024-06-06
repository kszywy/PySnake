from globals import MOVE_DISTANCE, STARTING_POSITION, Y_AXIS, X_AXIS, SNAKE_LENGTH
from turtle import Turtle


class Snake:

    def __init__(self, length: int):
        self.segments = []
        x_cor = STARTING_POSITION[0]

        for i in range(length):
            if i == 0:
                self.segments.append(Turtle("triangle"))
            else:
                self.segments.append(Turtle("square"))
            self.segments[i].color('white')
            self.segments[i].penup()
            self.segments[i].goto(x_cor, STARTING_POSITION[1])
            x_cor -= 20

        self.head = self.segments[0]

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

    def move_forward(self) -> None:
        self.move()
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self) -> None:
        last_heading = self.segments[-1].heading()
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()
        new_segment = self.segments[-1].clone()
        new_segment.shape("square")
        if last_heading == 0:
            x_cor -= 20
        elif last_heading == 90:
            y_cor -= 20
        elif last_heading == 180:
            x_cor += 20
        elif last_heading == 270:
            y_cor += 20
        new_segment.goto(x_cor, y_cor)
        self.segments.append(new_segment)

    def which_segment_is_bitten(self) -> int:
        for i in range(1, len(self.segments)):
            if self.head.distance(self.segments[i]) <= 15:
                return i
        return 0

    @staticmethod
    def which_enemy_segment_is_bitten(player, snake) -> int:
        for i in range(len(snake.segments)):
            if player.head.distance(snake.segments[i]) <= 15:
                return i
        return -1

    # Turtle module does not have a method for removing a Turtle object
    def eat_tail(self, bitten_segment_index: int) -> None:
        for i in range(len(self.segments) - 1, bitten_segment_index - 1, -1):
            self.segments[i].hideturtle()
            self.segments[i].goto(-4000, -4000)
            self.segments.pop(i)

    @staticmethod
    def enemy_collision(bitten_segment_index: int, snake) -> None:
        for i in range(len(snake.segments) - 1, bitten_segment_index - 1, -1):
            snake.segments[i].hideturtle()
            snake.segments[i].goto(-4000, -4000)
            snake.segments.pop(i)

    def is_dead(self) -> bool:
        if len(self.segments) == 0:
            return True
        return False

    def die(self, length: int) -> None:

        for i in range(len(self.segments) - 1, -1, -1):
            self.segments[i].hideturtle()
            self.segments[i].goto(-4000, -4000)
            self.segments.pop(i)
        self.__init__(SNAKE_LENGTH)

    def is_wall_hit(self) -> bool:
        y_cor = self.head.ycor()
        x_cor = self.head.xcor()
        if -X_AXIS + 20 > x_cor or x_cor > X_AXIS - 20 or -Y_AXIS + 20 > y_cor or y_cor > Y_AXIS - 20:
            return True
        return False

    def loop_board(self) -> None:
        y_cor = self.head.ycor()
        x_cor = self.head.xcor()
        if -X_AXIS + 20 > x_cor or x_cor > X_AXIS - 20:
            self.move()
            self.head.goto(-x_cor, y_cor)
        if -Y_AXIS + 20 > y_cor or y_cor > Y_AXIS - 20:
            self.move()
            self.head.goto(x_cor, -y_cor)

    def right(self) -> None:
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self) -> None:
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self) -> None:
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self) -> None:
        if self.head.heading() != 90:
            self.head.setheading(270)
