# Simple Notepad using tkinter

# [GUI Requirement]
# 1. title: Untitled - YJ Notepad
# 2. Menu: File, Edit, Format, View, Help
# 3. Working Menu: Open, Save, Exit in the File menu
# 3-1. Open: Open and show the content of mynote.txt
# 3-2. Save: Save the text content into the mynote.txt
# 3-3. Exit: Finish the Notepad
# 4. The text box is empty in the beginning
# 5. Window should be resizable
# 6. Insert the scroll bar on the right side

from tkinter import *
from tkinter.filedialog import asksaveasfile
import tkinter.messagebox
import os
from os import system

root = Tk()
root.title("Untitled - YJ Notepad")
root.geometry("640x480")  # Set the size
# root.geometry("640x480+300+300")  # Set the size and the position x:300, y:300
# root.resizable(True, True)  # Can not change the width, height - without resizable we can change the size of the window

filename = "mynote.txt"

menu = Menu(root)

# frame = Frame(root)
# frame.pack(side="bottom")

# Scroll Bar
# scrollbar = Scrollbar(frame)
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# txt = Text(frame, height=480, width=640, yscrollcommand=scrollbar.set)
# txt.pack(side="left")

# Text box
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)


def open_file(filename=None):
    if not filename:
        filename = tkinter.filedialog.askopenfilename()
    else:
        filename = filename

    if not (filename == ''):
        with open(filename, "r") as text_file:
            file_content = text_file.read()
            txt.delete("1.0", END)
            txt.insert(END, file_content)


def save_file():
    content = txt.get("1.0", END)
    file = asksaveasfile(defaultextension=".txt")
    file.write(content)


# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)


# Edit, Format, View, Help (No sub menus)
menu.add_cascade(label="Edit")
menu.add_cascade(label="Format")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
