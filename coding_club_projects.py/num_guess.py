import random


random_num = random.randint(1,100)

user_input = int(input("Enter a number between 1 and 100: "))

if user_input > random_num:
    print("Too High")
    dif = user_input - random_num
    print(f"    - You were {dif} away! ")
    print(f"    - The number was {random_num}! ")

elif user_input < random_num:
    print("Too Low")
    dif = random_num - user_input
    print(f"    You were {dif} away! ")
    print(f"    The number was{random_num}")

elif user_input == random_num:
    print("You got the number correct! ")
    
else:
    print("Invalid Input.")
