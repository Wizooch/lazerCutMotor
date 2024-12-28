#!/usr/bin/env python3

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World")

# Create and pack a label with "Hello World!"
label = tk.Label(root, text="Hello World!")
label.pack(padx=20, pady=20)

# Run the main event loop
root.mainloop()
