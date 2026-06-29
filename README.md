tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✓" if t["completed"] else "✗"
                print(f"{i}. {t['task']} [{status}]")

    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter updated task: ")
                tasks[index]["task"] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Deleted task: {removed['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        if not tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")
            index = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")
