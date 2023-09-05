import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40, font=("Helvetica", 16))
        self.task_list.pack(padx=10, pady=10)

        button_font = ("Helvetica", 14)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=button_font, width=20)
        self.add_button.pack(padx=10, pady=5)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task, font=button_font, width=20)
        self.edit_button.pack(padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=button_font, width=20)
        self.remove_button.pack(padx=10, pady=5)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks, font=button_font, width=20)
        self.clear_button.pack(padx=10, pady=5)

    def add_task(self):
        add_task_dialog = tk.Toplevel(self.root)
        add_task_dialog.title("Add Task")

        task_label = tk.Label(add_task_dialog, text="Enter task:")
        task_label.pack(padx=10, pady=10)

        task_text = tk.Text(add_task_dialog, height=5, width=40)
        task_text.pack(padx=10, pady=10)

        add_button = tk.Button(add_task_dialog, text="Add", command=lambda: self._add_task_from_dialog(task_text.get("1.0", tk.END)))
        add_button.pack(padx=10, pady=5)

    def _add_task_from_dialog(self, task):
        if task.strip():
            self.task_list.insert(tk.END, task.strip())
        self.root.focus_set()

    def edit_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            current_task = self.task_list.get(selected_task_index)

            edit_task_dialog = tk.Toplevel(self.root)
            edit_task_dialog.title("Edit Task")

            task_label = tk.Label(edit_task_dialog, text="Edit task:")
            task_label.pack(padx=10, pady=10)

            task_text = tk.Text(edit_task_dialog, height=5, width=40)
            task_text.insert(tk.END, current_task)
            task_text.pack(padx=10, pady=10)

            edit_button = tk.Button(edit_task_dialog, text="Save", command=lambda: self._edit_task_from_dialog(selected_task_index, task_text.get("1.0", tk.END)))
            edit_button.pack(padx=10, pady=5)

    def _edit_task_from_dialog(self, index, new_task):
        if new_task.strip():
            self.task_list.delete(index)
            self.task_list.insert(index, new_task.strip())
        self.root.focus_set()  # Return focus to the main window

    def remove_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.task_list.delete(selected_task_index)

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
