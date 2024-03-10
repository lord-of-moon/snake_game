from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.score = 0
        with open("/Users/demongod/Documents/snake game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-self.screen.window_width() / 2 + 10, self.screen.window_height() / 2 - 30)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 24, "normal"))
        self.goto(self.screen.window_width() / 2 - 150, self.screen.window_height() / 2 - 30)
        self.write(f"High Score: {self.high_score}", align="right", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/demongod/Documents/snake game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 36, "normal"))
        self.goto(0, -50)
        self.write(f"Your Score: {self.score}", align="center", font=("Arial", 24, "normal"))
