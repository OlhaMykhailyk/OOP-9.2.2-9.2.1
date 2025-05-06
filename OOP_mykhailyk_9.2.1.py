import tkinter.messagebox
from tkinter import *
from tkinter import ttk

class App:
    def __init__(self):
        self.root = Tk()
        self.form = ttk.Frame(self.root, padding=10)
        self.form.grid()
        self.draw()

    def check(line):
        is_palindrome = line == line[::-1]
        tkinter.messagebox.showinfo(title="###", message="It is palindrome" if is_palindrome else "It's not palindrome")

    def draw(self):
        label = ttk.Label(self.form, text="Check whether the line is palindrome")
        edit_box = ttk.Entry(self.form)
        quit_button = ttk.Button(self.form, text="Quit", command=self.root.destroy)
        check_button = ttk.Button(self.form, text="Check", command=lambda: App.check(edit_box.get()))

        label.pack()
        edit_box.pack()
        quit_button.pack()
        check_button.pack()

        self.root.mainloop()


if __name__ == "__main__":
    w = App()