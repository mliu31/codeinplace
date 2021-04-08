from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
Goal is to create a spiral of beepers 
"""

def main():
    while front_is_clear() and no_beepers_present():
        drop_beeper()
        turn_left()
        detect_beeper()


def drop_beeper():
    while front_is_clear() and no_beepers_present():
        put_beeper()
        move()


def detect_beeper():
    if beepers_present():
        turn_left()
        move()
        pick_beeper()
        move()
        turn_around()
        turn_left()
        move()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
