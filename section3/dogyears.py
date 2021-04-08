def main():
  human_age = float(input('Enter human age: '))
  dog_age = convert_to_dog(human_age)
  print('Dog age is: ', dog_age)

def convert_to_dog(human_age):
  return human_age * 7

if __name__ == '__main__':
  main()