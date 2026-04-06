# TO-DO LIST APPLICATION

tasks = ["Study Python", "Do Homework"]

def show_menu():
    print("\n==============================")
    print("      TO-DO LIST APP")
    print("==============================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("\nEnter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to mark as done: "))
        if 0 < task_no <= len(tasks):
            if "✔ Done" not in tasks[task_no - 1]:
                tasks[task_no - 1] = tasks[task_no - 1] + " ✔ Done"
                print("Task marked as done!")
            else:
                print("Task already completed!")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

# MAIN LOOP
while True:
    show_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")