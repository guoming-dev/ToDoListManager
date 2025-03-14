import unittest
import json
import os
from todo import Task, TodoList

class TestTodoList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Runs once before all tests.
        cls.test_file = "test_tasks.json"   # Use a test file
        cls.todo = TodoList()
        cls.todo.TASK_FILE = cls.test_file  # Override file for testing
        cls.todo.tasks = [] # Start with an empty task list

    @classmethod
    def tearDownClass(cls):
        # Runs once after all tests.
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)    # Clean up test file

    def setUp(self):
        # Runs before each test, resets task list.
        self.todo.tasks = []

    def test_list_task(self):
        # Test listing tasks.
        self.todo.add_task("Write documentation", priority=1)
        self.todo.add_task("Fix bugs", priority=3)
        self.assertEqual(len(self.todo.tasks), 2)

    def test_complete_task(self):
        # Test marking a task as completed.
        self.todo.add_task("Learn OOP", priority=2)
        self.todo.complete_task(1)  # Completing first task
        self.assertTrue(self.todo.tasks[0].done)    # Task should be marked as done

    def test_remove_task(self):
        # Test removing a task.
        self.todo.add_task("Refactor code", priority=3)
        self.todo.remove_task(1)    # Removing first task
        self.assertEqual(len(self.todo.tasks), 0)

    def test_clear_completed_tasks(self):
        # Test clearing only completed tasks.
        self.todo.add_task("Read book", priority=3)
        self.todo.add_task("Write blog", priority=1)
        self.todo.complete_task(1)  # Mark first task as done
        self.todo.clear_completed_tasks()
        self.assertEqual(len(self.todo.tasks), 1)   # Only one task should remain
        self.assertFalse(self.todo.tasks[0].done)   # Remaining task should be incomplete

    def test_task_persistence(self):
        # Test if tasks are correctly saved and loaded.
        self.todo.add_task("Test persistence", priority=2)
        self.todo.save_tasks()

        # Reload tasks from file
        new_todo = TodoList()
        new_todo.TASKS_FILE = self.test_file    # Load test file
        new_todo.tasks = new_todo.load_tasks()

        self.assertEqual(len(new_todo.tasks), 1)
        self.assertEqual(new_todo.tasks[0].description, "Test persistence")

if __name__ == "__main__":
    unittest.main()
