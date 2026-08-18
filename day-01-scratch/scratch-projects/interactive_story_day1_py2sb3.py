"""Day 1 Interactive Story — py2sb3 source (generates valid Scratch blocks).

Message name uses an underscore in Python (scene_2). The build script
renames it to the memo name (scene 2).

Class StageBackdrops is merged onto the real Stage after compile.

Arrow scripts check the backdrop name so the first press is Road and
the second is School (both sprites hear the right-arrow hat).
"""

from scratch.dsl import *


class StageBackdrops:
    def when_flag_clicked(self):
        switch_backdrop("Home")

    def when_broadcast_scene_2(self):
        switch_backdrop("Road")


class Child:
    def when_flag_clicked(self):
        show()
        go_to_xy(-80, -60)
        switch_backdrop("Home")
        say_for_secs("I missed the taxi. I am late for school.", 2)

    def when_clicked(self):
        say_for_secs("I need help. Press the right arrow.", 2)

    def when_key_right(self):
        if backdrop_name() == "Home":
            broadcast("scene_2")
            hide()


class Friend:
    def when_flag_clicked(self):
        hide()
        go_to_xy(80, -60)

    def when_broadcast_scene_2(self):
        show()
        say_for_secs("Walk with me. Press the arrow again.", 2)

    def when_key_right(self):
        if backdrop_name() == "Road":
            next_backdrop()
            say_for_secs("We arrived on time. Next time I will leave earlier.", 2)
