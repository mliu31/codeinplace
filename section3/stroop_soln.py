import random
import time
from termcolor import colored
from colorama import init
init(autoreset=True)

PHASE_TIME_S = 10

def main():
    print_intro()
    n_correct_control = run_phase(True)
    n_correct_flipped = run_phase(False)
    print('\nDone!')
    print('control', n_correct_control)
    print('flipped', n_correct_flipped)

def run_phase(is_phase_1):
    '''
    Ask a user questions for PHASE_TIME seconds. Return how many
    questions the user got correct.
    '''
    start_time = time.time()
    n_correct = 0
    while time.time() - start_time < PHASE_TIME_S:
        is_correct = run_single_test(is_phase_1)
        if is_correct:
            n_correct += 1
    return n_correct

def run_single_test(is_phase_1):
    '''
    Run a single test of a Stroop test. Takes in a boolean parameter
    is_phase_1 which is True if you are in phase 1 of the test. This
    function should return if the user was correct (again boolean).
    '''
    print('')
    color_name = random_color_name()
    font_color = get_font_color(color_name, is_phase_1)
    print_in_color(color_name, font_color)
    response = input('What color ink is the word written in? ')
    if response != font_color:
        print('Correct answer was: ' + font_color)
    return response == font_color

def get_font_color(color_name, is_phase_1):
    '''
    Return a font color. If phase1, return the same color as the
    color_name. Otherwise chose a random color. 
    '''
    if is_phase_1:
        return color_name
    while True: 
        next_choice = random_color_name()
        if next_choice != color_name:
            return next_choice

def print_intro():
    '''
    Function: print intro
    Prints a simple welcome message
    '''
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('pink', 'pink')

def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'pink'])

def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'pink': # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


if __name__ == '__main__':
    main()