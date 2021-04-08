"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    game_over = "yes"
    while game_over == "yes":
        start()
        game_over = input('\n\tDo you want to play again? \n\tPlease input "yes" or "no."\n>>')

def start():
    global num_stones, turns, mult_or_cpu
    num_stones = 20
    turns = 0
    mult_or_cpu = int(input("\tWelcome to NIMM!!! \n\tWould you like to play \n\t1. multiplayer \n\t2. vs CPU\n>>"))
    if mult_or_cpu == 1:
        multiplayer()
    elif mult_or_cpu == 2:
        cpu()
    else:
        mult_or_cpu = int(input("please input 1 (multiplayer) or 2 (CPU) "))
    decide_winner()


def cpu():
    global num_stones, turns, player
    while num_stones > 0:
        print("\nthere are " + str(num_stones) + " stone(s) left")
        if turns % 2 == 0:
            player = "CPU"
            if num_stones%3 == 1 or num_stones%3 == 0:
                take_num = 2
            else:
                take_num = 1
            print("the computer takes " + str(take_num) + " stone(s).")
        else:
            player = "Player 2"
            take_num = int(input(player + " would you like to remove 1 or 2 stones?\n>>"))
            while take_num != 1 and take_num != 2:
                take_num = int(input("Please enter only 1 or 2"))

        turns += 1
        num_stones = num_stones - take_num

def multiplayer():
    global num_stones, turns, player
    while num_stones > 0:
        print("there are "+ str(num_stones) + " stone(s) left")
        if turns%2 == 0:
            player = "Player 1"
        else:
            player = "Player 2"
        turns += 1
        take_num = int(input(player + " would you like to remove 1 or 2 stones?"))
        while take_num != 1 and take_num!= 2:
            take_num = int(input("Please enter only 1 or 2."))
        num_stones = num_stones - take_num

def decide_winner():
    if player == "Player 1" or player == "CPU":
        print("Player 2 wins!")
    if player == "Player 2":
        print("Player 1/CPU wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
