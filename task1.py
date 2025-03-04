import tkinter as tk
import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        del tasks[selected_task_index]
        save_tasks(tasks)
    except IndexError:
        pass

tasks = load_tasks()
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

for task in tasks:
    listbox.insert(tk.END, task)

root.mainloop()
