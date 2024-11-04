import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # List to store tasks
        self.tasks = []

        # Frame for tasks
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Attach scrollbar to listbox
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry box to add tasks
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Remove task button
        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()