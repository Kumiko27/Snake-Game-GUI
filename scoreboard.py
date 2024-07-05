from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.read_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {str(self.score)} High Score: {str(self.high_score)}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def write_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
