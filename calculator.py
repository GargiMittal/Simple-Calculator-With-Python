import tkinter as tk

def on_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and output
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                       command=lambda value=text: on_click(value) if value != "=" else calculate())
    button.grid(row=row, column=column, sticky="nsew")

# Configure row and column weights so that they expand proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
