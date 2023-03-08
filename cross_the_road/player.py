from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        # self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("green")
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)

    def lleft(self):
        self.setheading(180)
        self.forward(20)

    def rright(self):
        self.setheading(0)
        self.forward(20)

    def hit_or_not(self, cars):
        for car in cars:
            if car.distance(self) < 30 and car.ycor() - 25 <= self.ycor() <= car.ycor() + 18:
                return False
        return True

    def check_if_won(self):
        if self.ycor() >= 300:
            return True
        else:
            return False

    def print_message(self, message):
        self.hideturtle()
        self.goto(0, 0)
        self.color("black")
        self.write(arg=message, font=("Arial", 30, "normal"), align="center")

    def print_level(self, lvl):
        self.clear()
        self.hideturtle()
        self.color("black")
        self.goto(-380, 260)
        self.write(arg=f"Level {lvl}", font=("Arial", 12, "normal"), align = "center")
        self.goto(0, -300)
        self.color("green")
        self.showturtle()
