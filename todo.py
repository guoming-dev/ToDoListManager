# 1. Import necessary modules (argparse, json, os, colorama)
import json
import os
import argparse
from colorama import Fore, Style, init
init(autoreset=True)

TASKS_FILE = "tasks.json"

# 2. Define a function to load tasks from a JSON file
def load_tasks():
    # Load tasks from the JSON file.
    if not os.path.exists(TASKS_FILE):  # File does not exist
        return []
    
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:    # File exists but is empty or invalid 
            return []

# 3. Define a function to save tasks to a JSON file
def save_tasks(tasks):
    # Save tasks to the JSON file.
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# 4. Implement command-line argument parsing to handle user inputs
def parse_arguments():
    # Parse command-line arguments.
    parser = argparse.ArgumentParser(description="Command-Line Todo List Manager")

    parser.add_argument("--add", metavar="task", type=str, help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", metavar="task_id", type=int, help="Mark a task as completed")
    parser.add_argument("--remove", metavar="task_id", type=int, help="Remove a task")
    parser.add_argument("--clear", action="store_true", help="Clear all completed tasks")

    return parser.parse_args()

# 5. Implement add_task() function to add a new task
def add_task(task):
    # Add a new task to the list.
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"{Fore.GREEN}✅ Task added: {task}{Style.RESET_ALL}")

# 6. Implement list_tasks() function to display all tasks
def list_tasks():
    # List all tasks.
    tasks = load_tasks()
    if not tasks:
        print(f"{Fore.YELLOW}📁 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = f"{Fore.GREEN}✅" if task["done"] else f"{Fore.RED}❌"
        print(f"{Fore.CYAN}{i}, {status} {task['task']}{Style.RESET_ALL}")

# 7. Implement complete_task() function to mark a task as done
def complete_task(task_id):
    # Mark a task as completed.
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]["done"] = True
        save_tasks(tasks)
        print(f"{Fore.BLUE}✔️ Task {task_id} marked as completed.")
    else:
        print(f"{Fore.RED}⚠️ Invalid task ID.")
        
# 8. Implement remove_task() function to delete a task        
def remove_task(task_id):
    # Remove a task from the list.
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        removed = tasks.pop(task_id - 1)
        save_tasks(tasks)
        print(f"{Fore.RED}🗑️ Task removed: {removed['task']}")
    else:
        print(f"{Fore.RED}⚠️ Invalid task ID.")

# 9. Implement clear_completed_tasks() function to remove all completed tasks
def clear_completed_tasks():
    # Remove all completed tasks.
    tasks = load_tasks()
    tasks = [task for task in tasks if not task["done"]]
    save_tasks(tasks)
    print(f"{Fore.MAGENTA}🧹 Cleared all completed tasks.")

# 10. Main function to handle user commands
def main():
    args = parse_arguments()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.complete:
        complete_task(args.complete)
    elif args.remove:
        remove_task(args.remove)
    elif args.clear:
        clear_completed_tasks()
    else:
        print("ℹ️ Use --help to see available commands.")

# 11. Execute the main function to run the CLI application
if __name__ == "__main__":
    main()