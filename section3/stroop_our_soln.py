import random
import time
from colorama import init
from termcolor import colored
init(autoreset=True)

PHASE_LENGTH = 10 #in seconds

def main():
    print_intro()
    # Your solution goes here
    print(run_phase(True))


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

def run_single_test(is_phase_1):
    # choose the word and the color
    word = random_color_name()
    
    if is_phase_1:
        font_color = word
    else:
        font_color = random_color_name()
        
    # print it out
    print_in_color(word, font_color)
    
    # prompt the user for answer
    user_answer = input("What color ink is the word written in: ")
    
    # check that answer
    correct = user_answer == font_color
    return correct

def run_phase(is_phase_1):
    # get start time
    start_time = time.time()
    end_time = start_time + PHASE_LENGTH
    
    num_correct_tests = 0
    
    # stop at the end time
    while time.time() < end_time: 
        # run a test
        if run_single_test(is_phase_1):
            # collect number of correct
            num_correct_tests += 1 
    
    return num_correct_tests
    

if __name__ == '__main__':
    main()