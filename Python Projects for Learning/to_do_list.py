print("Welcome to the To-Do List App!")

tasks = []

while True:
    print("\nWhat action would you like to perform? (add/view/remove/edit/due_date/complete/exit): ")
    option = input().strip().lower()

    if option in ["add", "a"]:
        task_name = input("Enter the task name: ").strip()
        if not task_name:
            print("Task name cannot be empty.")
            continue

        due_date = input("Enter the due date (YYYY-MM-DD) or press Enter to skip: ").strip()
        task = {
            "name": task_name,
            "due_date": due_date if due_date else "No due date",
            "completed": False,
        }
        tasks.append(task)
        print(f"Task '{task_name}' added to the list.")

    elif option in ["view", "v"]:
        if not tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{index}. [{status}] {task['name']} | Due: {task['due_date']}")

    elif option in ["remove", "r"]:
        if not tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['name']}")

            try:
                task_number = int(input("Enter the number of the task you want to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task['name']}' removed from the list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif option in ["edit", "e"]:
        if not tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['name']}")

            try:
                task_number = int(input("Enter the number of the task you want to edit: "))
                if 1 <= task_number <= len(tasks):
                    old_name = tasks[task_number - 1]["name"]
                    new_name = input(f"Enter the new name for '{old_name}' or press Enter to keep it: ").strip()
                    if new_name:
                        tasks[task_number - 1]["name"] = new_name

                    new_due_date = input(
                        f"Enter the new due date for '{tasks[task_number - 1]['name']}' or press Enter to keep current date '{tasks[task_number - 1]['due_date']}': "
                    ).strip()
                    if new_due_date:
                        tasks[task_number - 1]["due_date"] = new_due_date

                    print(f"Task {task_number} updated.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif option in ["due_date", "d"]:
        if not tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['name']}")

            try:
                task_number = int(input("Enter the number of the task you want to update: "))
                if 1 <= task_number <= len(tasks):
                    new_due_date = input("Enter the new due date (YYYY-MM-DD): ").strip()
                    tasks[task_number - 1]["due_date"] = new_due_date if new_due_date else "No due date"
                    print(f"Due date updated for '{tasks[task_number - 1]['name']}'.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif option in ["complete", "c"]:
        if not tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['name']}")

            try:
                task_number = int(input("Enter the number of the task you want to mark as complete: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    print(f"Task '{tasks[task_number - 1]['name']}' marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif option in ["exit", "x"]:
        print("Exiting the To-Do List App. Goodbye!")
        break

    else:
        print("Invalid option. Please choose add, view, remove, edit, due_date, complete, or exit.")
