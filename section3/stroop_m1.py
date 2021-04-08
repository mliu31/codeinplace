import random
import time
from colorama import init
from termcolor import colored
init(autoreset=True)


def main():
    print_intro()
    run_single_test(True)
    run_single_test(False)

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
    color_name. Otherwise chose a random color. TODO: change this
    function to always return a different name in phase_2
    '''
    if is_phase_1:
        return color_name
    return random_color_name()

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