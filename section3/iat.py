import time
import random

TEST_LENGTH_S = 10

'''
This is an alternative program for sections where you are concerned 
about colorblindness getting in the way. It is basically the exact same
problem. We will get you a handout with details Monday night PDT.

recall that students don't know lists yet!
'''

def main():
    n_forward = run_phase(False)
    print('\n====================\n')
    n_backward = run_phase(True)

    print('standard', n_forward)
    print('flipped', n_backward)

def run_phase(flipped):
    print_intro(flipped)
    start_time = time.time()
    n_correct = 0
    while time.time() - start_time < PHASE_TIME_S:
        is_correct = run_single_test(is_phase_1)
        if is_correct:
            n_correct += 1
    return n_correct

def run_single_test(flipped):
    print('')
    animal = random_animal()
    association = get_association(animal, flipped)
    print(animal)
    response = input('Type the association: ')
    if response != association:
        print('Correct answer was ' + association)
    return response == association 

def print_intro(flipped):
    if flipped:
        print('Association test, standard')
    else:
        print('Association test, flipped!')
    print('You will be asked to answer three questions.')
    print('You should associate animals as follows:')
    print('puppy', get_association('puppy', flipped))
    print('panda', get_association('panda', flipped))
    print('spider', get_association('spider', flipped))
    print('bat', get_association('bat', flipped))
    input('Press enter to start... ')

def random_animal():
    return random.choice(['puppy', 'panda', 'spider', 'bat'])

def get_association(animal, flipped):
    if animal == 'puppy' or animal == 'panda':
        if flipped:
            return 'scary'
        else:
            return 'cute'
    if animal == 'bat' or animal == 'spider':
        if flipped:
            return 'cute'
        else:
            return 'scary'


if __name__ == '__main__':
    main()