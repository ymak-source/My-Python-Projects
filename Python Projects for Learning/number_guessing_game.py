import random

random_number = random.randint(1,100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess > random_number:
        print("Too High!")
    elif guess < random_number:
        print("Too Low!")
    elif guess == random_number:
        print("Congrats! You guessed the number!")
        break
    else:
        print("Invalid input! Please enter a number")
    