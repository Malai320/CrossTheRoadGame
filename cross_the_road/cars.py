from turtle import Turtle
from random import choice, randint


class Cars():
    def __init__(self):
        self.velocity = 3
        self.color_list = ["red", "blue", "green", "purple", "cyan", "yellow"]
        self.cars = []
        self.coordinates = []
        for i in range(20):
            self.add_car()

    def add_car(self):
        turtle = Turtle("square")
        turtle.color(choice(self.color_list))
        turtle.penup()
        turtle.shapesize(stretch_len=2, stretch_wid=1)
        turtle.setheading(180)
        self.coordinates.append((randint(-410, 410), randint(-240, 270)))
        turtle.goto(self.coordinates[-1])
        self.cars.append(turtle)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.velocity)
        for car in self.cars:
            if car.xcor() < -440:
                car.goto(440, randint(-240, 270))
