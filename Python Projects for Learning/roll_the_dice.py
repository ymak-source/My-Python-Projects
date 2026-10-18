import random

num_of_dice_rolls_so_far = 0
while True:
    
    choice = input("Roll the dice? (y/n): ")
    if choice.lower() == "y":

        num_of_dice_rolls_so_far += 1 
        random_number = random.randint(1,6)
        random_number_2 = random.randint(1,6)
        print(f"({random_number},{random_number_2})")
        print(f"(That was dice roll number {num_of_dice_rolls_so_far})")
    elif choice.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input!")


