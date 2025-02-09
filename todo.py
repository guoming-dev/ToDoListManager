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

    # Add priority argument (Optional, defaults to Low)
    parser.add_argument("--priority", metavar="level", type=int, choices=[1, 2, 3],
                        help="Set task priority: 1 (High), 2 (Medium), 3 (Low)")

    parser.add_argument("--add", metavar="task", type=str, help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", metavar="task_id", type=int, help="Mark a task as completed")
    parser.add_argument("--remove", metavar="task_id", type=int, help="Remove a task")
    parser.add_argument("--clear", action="store_true", help="Clear all completed tasks")

    return parser.parse_args()

# 5. Implement add_task() function to add a new task
def add_task(task, priority=None):
    """
    Adds a new task to the task list with a given priority level.
    If no priority is provided, defaults to 3 (Low).
    Priority Levels: 
    - 1 (High) 🔥
    - 2 (Medium) ⚡️
    - 3 (Low) ✅
    """
    tasks = load_tasks()    # Load existing tasks

    # ✅ Set default priority to 3 (Low) if not provided
    if priority is None:
        priority = 3

    # ✅ Validate priority input (Only accept 1, 2, or 3)
    if priority not in [1, 2, 3]:
        print(f"{Fore.RED} ⚠️ Invalid priority! Use 1 (High), 2 (Medium), or 3 (Low).")
        return

    # Append task with priority field
    tasks.append({"task": task, "done": False, "priority": priority})
    save_tasks(tasks)   # Save tasks back to file
    
    print(f"{Fore.GREEN}✅ Task added: {task} (Priority: {priority}){Style.RESET_ALL}")

# 6. Implement list_tasks() function to display all tasks
def list_tasks():
    """
    Lists all tasks sorted by priority.
    Displays ✅ for completed tasks and ❌ for pending tasks.
    """
    tasks = load_tasks()
    if not tasks:
        print(f"{Fore.YELLOW}📁 No tasks found.")
        return
    
    # 🏷️ Priority labels for readability
    priority_labels = {
        1: "🔥 High",
        2: "⚡️ Medium",
        3: "✅ Low"
    }
    # 🔄 Sort tasks by priority (ascending: 1 → 3)
    tasks.sort(key = lambda t: t["priority"])

    # 🎨 Display sorted tasks
    for i, task in enumerate(tasks, 1):
        status = f"{Fore.GREEN}✅" if task["done"] else f"{Fore.RED}❌"
        priority_label = priority_labels.get(task["priority"], "❓ Unknown")
        print(f"{Fore.CYAN}{i}, {status} {task['task']} [{priority_label}]{Style.RESET_ALL}")

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
    """
    Main function to handle user input and execute the corresponding task actions.
    """
    args = parse_arguments()    # Parse command-line arguments

    if args.add:
        # 🏷️ If priority is not specified, set it to 3 (Low)
        priority = args.priority if args.priority is not None else 3
        add_task(args.add, priority)
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