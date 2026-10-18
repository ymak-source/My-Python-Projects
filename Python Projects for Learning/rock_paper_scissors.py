import random

my_list = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(my_list).lower()

user_choice = input("Please choose either Rock, Paper or Scissors: ").lower()

if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid Input. You should have entered Rock, Paper or Scissors")
    quit()
else:
    print(f"You chose {user_choice.capitalize()}")
    print(f"The 'computer' chose {computer_choice.capitalize()}")

if user_choice == computer_choice:
    print("Draw")
elif    (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You Win!")
else:
    print("You lose...Better luck next time!")