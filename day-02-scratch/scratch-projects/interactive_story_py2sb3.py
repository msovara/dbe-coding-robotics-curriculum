"""Interactive Story — py2sb3 source (generates valid Scratch blocks).

Message names use underscores in Python (scene_1). The build script
renames them to the memo names (scene 1). Same for story_choices.

Class StageBackdrops is merged onto the real Stage after compile.
"""

from scratch.dsl import *


class StageBackdrops:
    def when_flag_clicked(self):
        switch_backdrop("Laboratory")
        delete_all_of_list("story_choices")
        broadcast("scene_1")

    def when_broadcast_path_A(self):
        switch_backdrop("Forest")

    def when_broadcast_path_B(self):
        switch_backdrop("Space")

    def when_broadcast_ending_A(self):
        switch_backdrop("Ending A")

    def when_broadcast_ending_B(self):
        switch_backdrop("Ending B")


class Guide:
    def when_flag_clicked(self):
        show()
        go_to_xy(-100, -80)

    def when_broadcast_scene_1(self):
        say_for_secs("The laboratory alarm is sounding!", 2)
        ask("Do you investigate the forest (A) or launch into space (B)?")
        choice = answer()
        add_to_list(choice, "story_choices")
        if choice == "A" or choice == "a":
            broadcast("path_A")
        else:
            broadcast("path_B")
        hide()


class Scientist:
    def when_flag_clicked(self):
        hide()

    def when_broadcast_path_A(self):
        go_to_xy(20, -70)
        show()
        say_for_secs("The forest sensor has found an injured animal.", 2)
        ask("Help the animal? Type YES or NO.")
        add_to_list(answer(), "story_choices")
        if answer() == "yes" or answer() == "YES" or answer() == "Yes":
            say_for_secs("Your kindness saves the animal!", 2)
            hide()
            broadcast("ending_A")
        else:
            say_for_secs("You return to the laboratory.", 2)
            hide()
            broadcast("ending_B")


class Robot:
    def when_flag_clicked(self):
        hide()

    def when_broadcast_path_B(self):
        go_to_xy(30, -60)
        show()
        say_for_secs("An asteroid is approaching the spacecraft!", 2)
        ask("Use the shield? Type YES or NO.")
        add_to_list(answer(), "story_choices")
        if answer() == "yes" or answer() == "YES" or answer() == "Yes":
            say_for_secs("The shield protects the spacecraft!", 2)
            hide()
            broadcast("ending_A")
        else:
            say_for_secs("The crew returns safely to Earth.", 2)
            hide()
            broadcast("ending_B")
