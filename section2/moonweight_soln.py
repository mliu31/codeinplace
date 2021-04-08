"""
Write a program to prompt the user for a weight on earth and print
the equivalent weight on the moon.
"""
# we use constants!
MOON_GRAVITY = 0.165


def main():
    # get user input
    earth_weight_str = input("Enter a weight on Earth: ")

    # convert to float data type
    earth_weight = float(earth_weight_str)

    # do the math!
    moon_weight = MOON_GRAVITY * earth_weight

    # print to the user
    # notice the string concatenation
    print("Equivalent weight on the moon: " + str(moon_weight))

if __name__ == '__main__':
    main()