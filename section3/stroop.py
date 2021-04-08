import random
import time
from colorama import init
from termcolor import colored
init(autoreset=True)


def main():
    print_intro()
    # Your solution goes here

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