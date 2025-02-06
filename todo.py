import json
import os
import argparse
from colorama import Fore, Style, init
init(autoreset=True)

TASKS_FILE = "tasks.json"

def load_tasks():
    # Load tasks from the JSON file.
    if not os.path.exists(TASKS_FILE):  # File does not exist
        return []
    
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:    # File exists but is empty or invalid 
            return []
    
def save_tasks(tasks):
    # Save tasks to the JSON file.
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def parse_arguments():
    # Parse command-line arguments.
    parser = argparse.ArgumentParser(description="Command-Line Todo List Manager")

    parser.add_argument("--add", metavar="task", type=str, help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", metavar="task_id", type=int, help="Mark a task as completed")
    parser.add_argument("--remove", metavar="task_id", type=int, help="Remove a task")
    parser.add_argument("--clear", action="store_true", help="Clear all completed tasks")

    return parser.parse_args()

def add_task(task):
    # Add a new task to the list.
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def list_tasks():
    # List all tasks.
    tasks = load_tasks()
    if not tasks:
        print("📁 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}, {status} {task['task']}")

def complete_task(task_id):
    # Mark a task as completed.
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]["done"] = True
        save_tasks(tasks)
        print(f"☑️ Task {task_id} marked as completed.")
    else:
        print("⚠️ Invalid task ID. ")
        
def remove_task(task_id):
    # Remove a task from the list.
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        removed = tasks.pop(task_id - 1)
        save_tasks(tasks)
        print(f"🗑️ Task removed: {removed['task']}")
    else:
        print("⚠️ Invalid task ID.")

def clear_completed_tasks():
    # Remove all completed tasks.
    tasks = load_tasks()
    tasks = [task for task in tasks if not task["done"]]
    save_tasks(tasks)
    print("🧹 Cleared all completed tasks.")

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

if __name__ == "__main__":
    main()