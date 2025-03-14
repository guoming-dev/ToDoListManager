# Command-Line Todo List Manager

## 📌 Project Overview

The **Command-Line Todo List Manager** is a lightweight yet powerful Python-based CLI application designed to help users efficiently manage their tasks directly from the terminal. With a focus on **productivity, simplicity, and automation**, this tool provides a seamless experience for tracking and organizing daily tasks.

Built with **scalability and modularity** in mind, this project follows best software engineering practices, ensuring maintainability and future enhancements.

🎥 **Demo Video**: [Watch on YouTube](https://youtu.be/EaHFehEctIE)

---

## 🎯 Objectives

- 📝 **Efficient Task Management** - Create, list, complete, and remove tasks quickly via the command line.
- ⚙️ **Command-Line Arguments** - Implement `argparse` for robust CLI interactions.
- 💾 **Persistent Storage** - Save tasks locally using JSON for a lightweight, database-free solution.
- 🤖 **Automation** - Focus on providing users with core functionalities, such as adding, listing, and managing tasks efficiently, while building the foundation for potential future enhancements like scheduled reminders or notifications.
- 🛠️ **Scalability & Modularity** - Ensure clean, structured code that supports future enhancements.

---

## 🔧 Tech Stack

- Language: 🐍 Python 3.x
- Libraries:
  - `argparse` - Parsing command-line arguments
  - `json` - Storing task data in a structured format
  - `os` - File handling for task storage
  - `colorama` (optional) - Colored terminal output for better UI/UX
- Future Integrations:
  - 🔗 Notion, Google Tasks API for cloud sync
  - 💾 SQLite for structured database management

---

## 🚀 Features & Usage

### 💡 New Feature: Task Prioritization 

**Highlights**:
- Tasks can now have **priority levels**:
- Default priority: If no priority is specified, tasks default to **Low (3)**.
- Input validation ensures only valid priority levels (1, 2, or 3) are accepted.
- Tasks are automatically **sorted by priority** when listed.

### ✅ Basic Functionality

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>python todo.py --add "Task Name"</code></td>
        <td>➕ Adds a new task (defaults to Low Priority (3) if none is specified)</td>
    </tr>
    <tr>
        <td><code>python todo.py --list</code></td>
        <td>📋 Displays all tasks, sorted by <strong>priority</strong> (High → Low)</td>
    </tr>
    <tr>
        <td><code>python todo.py --complete 2</code></td>
        <td>✅ Marks task #2 as completed</td>
    </tr>
    <tr>
        <td><code>python todo.py --remove 3</code></td>
        <td>🗑️ Removes task #3</td>
    </tr>
    <tr>
        <td><code>python todo.py --clear</code></td>
        <td>🧹 Clears all completed tasks</td>
    </tr>
</table>

### 🏷️ Advanced Functionality

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>python todo.py --add "Task Name" --priority 1</code></td>
        <td>➕ Adds a new task with 🔥 <strong>High Priority (1)</strong></td>
    </tr>
    <tr>
        <td><code>python todo.py --add "Task Name" --priority 2</code></td>
        <td>➕ Adds a new task with ⚡️ <strong>Medium Priority (2)</strong></td>
    </tr>
    <tr>
        <td><code>python todo.py --add "Task Name" --priority 3</code></td>
        <td>➕ Adds a new task with ✅ <strong>Low Priority (3)</strong></td>
    </tr>
</table>

### 🛠️ Future Planned Enhancements

- ⏰ **Due Dates & Reminders** - Send notifications for upcoming tasks.
- 🔄 **Export & Import** - Sync tasks across devices via APIs.
- 🔁 **Recurring Tasks** - Automate repetitive task scheduling.
- 💎 **Subscription-Based Features** - Premium users get advanced filtering, analytics, and integrations.
- 📱 **Cross-Platform Sync** - Sync tasks across devices using cloud storage.

---

## 🏗️ System Architecture

### File Structure

```
📂 ToDoListManager
    |--- 📄 todo.py # Main CLI script
    |--- 📄 tasks.json  # Persistent task storage
    |--- 📄 README.md   # Documentation
    |--- 📄 requirements.txt    # Dependencies
```

### Design Considerations

- 🧩 **Separation of Concerns** - Logic is modular, avoiding monolithic code.
- ❌ **Error Handling** - Robust input validation and user-friendly messages.
- 💻 **Cross-Platform Support** - Works on Linux, MacOS, and Windows.

---

## Why I Built This Project

As a **self-taught Python developer**, this project follows industry standards and demonstrates:

- 💻 **Command-line automation expertise**
- 🛠️ **Best practices in CLI development & argument parsing**
- 💾 **Proficiency in handling data persistence**
- 🏗️ **Software architecture design & scalability**

This is an **excellent addition** to any portfolio, highlight **Python proficiency**, **problem-solving**, and **real-world applicability**.

---

## 📜 License

This project is licensed under the **MIT License** - feel free to contribute, fork, and improve!

---

## 🤝 Contributions & Feedback

- 🔧 **Pull Requests** - Open to feature suggestions & improvements.
- 🐞 **Issues** - Found a bug? Have an idea? Submit an issue!
- 💬 **Discussions** - Let's make CLI productivity tools better together!