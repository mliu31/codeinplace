"""
Write a program to simulate a magic eight ball. The program should
let the user type a yes or no question and pick a random answer from a
set of 6 predetermined answers.
"""
import random

def main():
    #get user input
    user_question = input("What is your question? ")

    #check to see if they are done (did they just hit enter"
    while user_question != "":
        # get random number
        rand_num = random.randint(1, 4)

        # if that number == something
        if rand_num == 1:
            print("Quarantine sucks")
        if rand_num == 2:
            print("Absolutely")
        if rand_num == 3:
            print("Only if you join code in place")
        if rand_num == 4:
            print("It depends")

        #set up for the next loop
        user_question = input("What is your question? ")



if __name__ == '__main__':
    main()