import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.title} ({self.category}): {self.description}"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal To-Do List")
        self.tasks = self.load_tasks()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks_to_listbox()

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear current list
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        title = simpledialog.askstring("Input", "Enter task title:")
        description = simpledialog.askstring("Input", "Enter task description:")
        category = simpledialog.askstring("Input", "Enter task category (e.g., Work, Personal):")
        
        if title and description and category:
            task = Task(title, description, category)
            self.tasks.append(task)
            self.load_tasks_to_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Please provide all task details.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.mark_completed()
            self.load_tasks_to_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.load_tasks_to_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                return [Task(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()