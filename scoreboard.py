from turtle import Turtle

ALIGNMENT = "center"
FONT = "Helvetica"
FONT_SIZE = 15
FONT_TYPE = "normal"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}",
                   False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.color("red")
    #     self.write("Game Over!", align="Center", font=("Arial", 30, "bold"))

    def clear_score(self):
        self.score += 1
        self.update_scoreboard()
