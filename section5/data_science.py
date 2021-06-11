# data comes from Johns Hopkins Univeristy. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# you can find data beyond cumulative cases there!

'''
Test your code by analysing total confirmed cases over time
Each line in the file represents one day. The first value is confirmed cases on Jan 22nd.
The number of confirmed cases is "cumulative" meaning that it is the total number
of cases up until the current day. It will never go down! 
'''
ITALY_PATH = 'italy.txt'

# this directory has files for all countries if you want to explore further
DATA_DIR = 'confirmed'

import matplotlib.pyplot as plt

def main():
    # milestone 1
    data = load_data()

    plt.plot(data)
    plt.title("Total infections in Italy")
    plt.xlabel("Days")
    plt.ylabel("Total infections")
    plt.show()
    
    # milestone 2
    count_non_zero(data)

    # milestone 3
    daily_change = calc_daily_change(data)

    plt.plot(daily_change)
    plt.title("New Infections per day in Italy")
    plt.xlabel("Days since first case")
    plt.ylabel("New Infections")
    plt.show()

def count_non_zero(data):
    n = 0
    for value in data:
        if value > 0:
            n += 1
    return n

def calc_daily_change(data):
    daily_change = []
    for i in range(1, len(data)):
        curr_value = data[i]
        prev_value = data[i - 1]
        change = curr_value - prev_value
        daily_change.append(change)
    return daily_change

def load_data():
    data = []
    file = open(ITALY_PATH)
    for line in file:
        value = int(line)
        data.append(value)
    return data

if __name__ == '__main__':
    main()