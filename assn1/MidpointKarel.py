from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    if front_is_clear():
        #for >1x1 grid cases
        put_initial_beepers()
        snake_bt_beepers()
    else:
        #accounts for 1x1 grid in which case, there is only one point which is the midpoint
        put_beeper()

def put_initial_beepers():
    #put beeper @ each end of the grid
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()

def snake_bt_beepers():
    #noves the beepers in one point at a time till it reaches the midpoint; while loop breaks karel's oscillation
    while no_beepers_present():
        while no_beepers_present():
          move()
        transition()
        put_beeper()
        move()
    transition()

def transition():
    #pickup beeper and change direction
    pick_beeper()
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
