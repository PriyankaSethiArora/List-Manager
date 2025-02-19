# To-Do List Manager

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to delete a task
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Exiting To-Do List Manager. Goodbye!")
                break
            else:
                print("Invalid choice, please select a valid option.")
        except ValueError:
            print("Please enter a valid number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
