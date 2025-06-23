tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for t in tasks:
            print("-", t)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
