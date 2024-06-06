from globals import Y_AXIS
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = Scoreboard.read_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, Y_AXIS - 20)
        self.update_score()

    @staticmethod
    def read_high_score() -> int:
        with open("globals.py", "r") as file:
            contents = file.readline().split()
            for i in range(len(contents)):
                if i == 2:
                    return int(contents[i])
        file.close()

    @staticmethod
    def update_high_score(new_high_score: int) -> None:
        with open("globals.py", "r") as file:
            contents = file.read().splitlines()
            strr = f"HIGH_SCORE = {new_high_score}"
            contents[0] = strr

        file.close()

        with open("globals.py", "w") as file:
            for line in contents:
                file.write(line + "\n")

        file.close()

    def update_score(self):
        self.write(f"Your score: {self.score} High score: {self.high_score}", move=False, align="center",
                   font=("Courier", 10, "bold"))

    def refresh(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def reset_score(self):
        self.score = 0
        if self.high_score > Scoreboard.read_high_score():
            Scoreboard.update_high_score(self.high_score)
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0, Y_AXIS - 40)
    #     self.color("green")
    #     self.write("\nGAME OVER", move=False, align="center", font=("Courier", 15, "bold"))
