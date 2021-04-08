"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    num_correct = 0
    while num_correct != 3:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        sum = num1 + num2
        answer = int(input("what is " + str(num1) + " + " + str(num2) + "\n>>"))

        if sum == answer:
            num_correct += 1
            print("Correct. You've gotten " + str(num_correct) + " problem(s) right in a row! ")
            if num_correct == 3:
                print("Congratulations! you've mastered addition")
        else:
            print("Incorrect. the expected answer is " + str(sum))
            num_correct = 0


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
