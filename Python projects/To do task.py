tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def delete_task(task_number):
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            print("Task deleted:", task)
        else:
            print("Task number out of range")
    except ValueError:
        print("Invalid task number")

def view_tasks():
    if not tasks:
        print("No tasks in the list")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    print("Options:")
    print("Enter 'add' to add a task")
    print("Enter 'delete' to delete a task")
    print("Enter 'view' to view tasks")
    print("Enter 'exit' to end the program")

    user_input = input(": ").capitalize()

    if user_input == "Exit":
        break
    elif user_input == "Add":
        task = input("Enter a task: ")
        add_task(task)
    elif user_input == "Delete":
        delete_option = input("Enter the task number or task name to delete: ")
        delete_task(delete_option)
    elif user_input == "View":
        view_tasks()
    else:
        print("Invalid input") 