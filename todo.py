import json
import os
import argparse
from colorama import Fore, Style, init

# ✅ Initialize colorama
init(autoreset=True)

TASKS_FILE = "tasks.json"

# 🎨 Priority labels with colors
PRIORITY_LABELS = {
    1: Fore.RED + "🔥 High" + Style.RESET_ALL,
    2: Fore.YELLOW + "⚡ Medium" + Style.RESET_ALL,
    3: Fore.GREEN + "✅ Low" + Style.RESET_ALL
}


class Task:
    def __init__(self, description, priority=3, done=False):    # ✅ Add done=False
        self.description = description
        self.priority = priority
        self.done = done    # ✅ Store the loaded "done" status

    def mark_complete(self):
        self.done = True

    def __str__(self):
        status = Fore.GREEN + "✅" if self.done else Fore.RED + "❌"
        return f"{Fore.CYAN}{status} {self.description} [{PRIORITY_LABELS[self.priority]}]{Style.RESET_ALL}"


class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def add_task(self, description, priority=3):
        if priority not in [1, 2, 3]:
            print(
                f"{Fore.RED}⚠️ Invalid priority! Use 1 (High), 2 (Medium), or 3 (Low).{Style.RESET_ALL}")
            return

        task = Task(description, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(
            f"{Fore.GREEN}✅ Task added: {description} ({PRIORITY_LABELS[priority]}){Style.RESET_ALL}")

    def list_tasks(self):
        if not self.tasks:
            print(f"{Fore.YELLOW}📁 No tasks found.{Style.RESET_ALL}")
            return

        self.tasks.sort(key=lambda t: t.priority)  # 🔄 Sort tasks by priority
        for i, task in enumerate(self.tasks, 1):
            print(f"{Fore.MAGENTA}{i}. {task}{Style.RESET_ALL}")

    def complete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1].mark_complete()
            self.save_tasks()
            print(
                f"{Fore.BLUE}✔️ Task {task_id} marked as completed.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}⚠️ Invalid task ID.{Style.RESET_ALL}")

    def remove_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            removed = self.tasks.pop(task_id - 1)
            self.save_tasks()
            print(
                f"{Fore.RED}🗑️ Task removed: {removed.description}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}⚠️ Invalid task ID.{Style.RESET_ALL}")

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.done]
        self.save_tasks()
        print(f"{Fore.MAGENTA}🧹 Cleared all completed tasks.{Style.RESET_ALL}")

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump([vars(task) for task in self.tasks], file, indent=4)

    def load_tasks(self):
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, "r") as file:
            try:
                return [Task(**task) for task in json.load(file)]
            except json.JSONDecodeError:
                return []


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Command-Line Todo List Manager")
    parser.add_argument("--add", metavar="task",
                        type=str, help="Add a new task")
    parser.add_argument("--priority", metavar="level", type=int,
                        choices=[1, 2, 3], help="Set task priority: 1 (High), 2 (Medium), 3 (Low)")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", metavar="task_id",
                        type=int, help="Mark a task as completed")
    parser.add_argument("--remove", metavar="task_id",
                        type=int, help="Remove a task")
    parser.add_argument("--clear", action="store_true",
                        help="Clear all completed tasks")
    return parser.parse_args()


def main():
    todo = TodoList()
    args = parse_arguments()

    if args.add:
        todo.add_task(args.add, args.priority or 3)
    elif args.list:
        todo.list_tasks()
    elif args.complete:
        todo.complete_task(args.complete)
    elif args.remove:
        todo.remove_task(args.remove)
    elif args.clear:
        todo.clear_completed_tasks()
    else:
        print(f"{Fore.CYAN}ℹ️ Use --help to see available commands.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
