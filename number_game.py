import random

secret_num = random.randint(1, 10)

while True:
    guess = int(input("Guess a numer from 1 to 10\n>"))
    if guess == secret_num:
        print("You got it! My number was {}".format(secret_num))
        break
    else:
        print("That's not it")