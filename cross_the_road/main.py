from turtle import Screen, Turtle
from cars import Cars
from player import Player
from time import sleep

screen = Screen()
screen.setup(height=600, width=850)
screen.tracer(0)
screen.listen()


def start_new_lvl():
    global corn
    corn = True


corn = True
cars = Cars()
player = Player()
enter_typer = Turtle()
enter_typer.hideturtle()
enter_typer.goto(-350, -276)

screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.rright, "Right")
screen.onkeypress(player.lleft, "Left")
screen.onkey(start_new_lvl, "Return")

game_on = True
victory = False
lvl = 1
player.print_level(lvl)

while game_on and not victory:
    if corn:
        sleep(0.1)
        enter_typer.clear()
        screen.onkeypress(player.up, "Up")
        screen.onkeypress(player.down, "Down")
        screen.onkeypress(player.rright, "Right")
        screen.onkeypress(player.lleft, "Left")
        cars.move_cars()
        victory = player.check_if_won()
        game_on = player.hit_or_not(cars.cars)
        if not game_on:
            player.print_message("Game Over")
        if victory:
            corn = False
            lvl += 1
            cars.velocity += 1
            player.print_level(lvl)
            victory = False
            enter_typer.write(arg="Press 'enter' to continue", font=("Arial", 20, "normal"))
    else:
        screen.onkeypress(None, "Up")
        screen.onkeypress(None, "Down")
        screen.onkeypress(None, "Right")
        screen.onkeypress(None, "Left")

    screen.update()

screen.exitonclick()
