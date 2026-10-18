operation = input("Enter an operation (+ - * /): ")
num_1 = input("Enter your first number:  ")
num_2 = input("Enter your second number: ")
decision = "y"

while decision == "y".lower():

    
    if operation == "+":
        print(num_1 + num_2)

    elif operation == "-":
        print(num_1 - num_2)
        decision = ("Would you like to continue? ( y/n) : ")

    elif operation == "*":
        print(num_1 * num_2)
        decision = ("Would you like to continue? ( y/n) : ")

    elif operation == "/":
        print(num_1 / num_2)
        decision = ("Would you like to continue? ( y/n) : ")

    else:
        print("Invalid input. Must be (+ - * / ): ")
        decision = ("Would you like to continue? ( y/n) : ")

if decision == "n".lower():
    print("Thanks for using my calculator! ")
    exit()