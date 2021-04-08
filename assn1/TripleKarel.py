from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""
def main():
    for i in range(2):
        paint_block()
        turn_left()
        turn_left()
        turn_left()
        put_beeper()
        move()
        #paints two blocks and has the same transition for both,, because of fencepost error, we run paintblock after the for loop
    paint_block()

def paint_side():
    while left_is_blocked():
        put_beeper()
        move()

def paint_block():
    for i in range(2):
        paint_side()
        turn_left()
        move()
    paint_side()
    #addresses fencepost error again in painting 2 sides and turning left and moving, then painting the last side
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
