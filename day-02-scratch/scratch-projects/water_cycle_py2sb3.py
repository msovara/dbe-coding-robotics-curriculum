"""Water Cycle — py2sb3 source (generates valid Scratch blocks).

Avoid `while not (...)` — py2sb3 compiles that as a broken `repeat until not`.
Use forever + if + stop, with cleanup *inside* the if, before stop.
"""

from scratch.dsl import *


class Sun:
    def when_flag_clicked(self):
        evaporated = 0
        condensed = 0
        precipitated = 0
        ground_water = 0
        go_to_xy(170, 120)
        show()

    def when_clicked(self):
        broadcast("evaporate")


class Droplet:
    def when_flag_clicked(self):
        go_to_xy(-100, -130)
        show()

    def when_broadcast_evaporate(self):
        show()
        while True:
            if y_position() > 90:
                hide()
                broadcast("condense")
                stop("this script")
            change_y(5)
            evaporated += 1
            wait(0.05)

    def when_broadcast_rain(self):
        go_to_xy(-70, 100)
        show()
        while True:
            if touching("Ground"):
                broadcast("collected")
                stop("this script")
            change_y(-6)
            precipitated += 1
            wait(0.05)

    def when_broadcast_collected(self):
        ground_water += 1
        go_to_xy(-100, -130)
        say_for_secs("Collection", 2)


class Cloud:
    def when_flag_clicked(self):
        go_to_xy(-70, 120)
        hide()

    def when_broadcast_condense(self):
        show()
        condensed += 1
        say_for_secs("Condensation", 2)
        wait(1)
        broadcast("rain")
        hide()


class Ground:
    def when_flag_clicked(self):
        go_to_xy(0, -140)
        show()
