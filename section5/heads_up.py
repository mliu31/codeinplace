import random

# the name of the file to read in!
FILE_NAME = 'cswords.txt'

def main():
    words = load_data()

    while True:
        input('Press enter for next word: ')
        print('')
        next_word = random.choice(words)
        print(next_word)

def load_data():
    words = []
    for line in open(FILE_NAME):
        word = line.strip()
        words.append(word)
    return words

if __name__ == '__main__':
    main()