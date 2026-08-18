"""Catch Game — py2sb3 source (generates valid Scratch blocks)."""

from scratch.dsl import *


class Basket:
    def when_flag_clicked(self):
        go_to_xy(0, -145)
        show()
        while True:
            if key_pressed("left arrow"):
                change_x(-10)
            if key_pressed("right arrow"):
                change_x(10)


class Fruit:
    def when_flag_clicked(self):
        hide()
        while True:
            create_clone("myself")
            wait(pick_random(1, 3))

    def when_i_start_as_clone(self):
        go_to_xy(pick_random(-200, 200), 170)
        show()
        while not (touching("Basket") or y_position() < -170):
            change_y(-5)
            wait(0.03)
        if touching("Basket"):
            score += 1
        delete_this_clone()


class Referee:
    def when_flag_clicked(self):
        score = 0
        hide()
        while True:
            wait(0.05)
            if score > 19:
                broadcast("win")
                stop("this script")

    def when_broadcast_win(self):
        show()
        say_for_secs("You win!", 3)
        stop("all")
