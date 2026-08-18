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
        say_for_secs("Click me, or wait...", 2)
        wait(1)
        broadcast("evaporate")

    def when_clicked(self):
        broadcast("evaporate")


class Droplet:
    def when_flag_clicked(self):
        go_to_xy(-100, -100)
        show()

    def when_broadcast_evaporate(self):
        go_to_xy(-100, -100)
        show()
        while True:
            change_y(5)
            wait(0.05)
            if y_position() > 90:
                evaporated += 1
                hide()
                broadcast("condense")
                stop("this script")

    def when_broadcast_rain(self):
        go_to_xy(-70, 100)
        show()
        while True:
            change_y(-6)
            wait(0.05)
            if touching("Ground") or y_position() < -150:
                precipitated += 1
                broadcast("collected")
                stop("this script")

    def when_broadcast_collected(self):
        ground_water += 1
        go_to_xy(-100, -100)
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
        go_to_xy(0, -165)
        show()
