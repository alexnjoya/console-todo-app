import os

tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 0 <= taskToDelete < len(tasks):
            deleted_task = tasks.pop(taskToDelete)
            print(f"Task '{deleted_task}' has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid task number.")

def saveTasks(filename):
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print("Error saving tasks:", e)

def loadTasks(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    tasks.append(line.strip())
        except Exception as e:
            print("Error loading tasks:", e)

if __name__ == "__main__":
    # Create file path for storing tasks in the user's working directory
    user_file = os.path.join(os.getcwd(), "todo_list.txt")
    print("File path:", user_file)

    # Load tasks from file if it exists
    loadTasks(user_file)

    print("Welcome to the to do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
            saveTasks(user_file)
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks() 
        elif choice == "4":
            print("Tasks saved. Goodbye! 👋👋")
            break
        else:
            print("Invalid input. Please try again.")
