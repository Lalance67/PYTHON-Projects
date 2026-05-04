import tkinter as tk

def clear():
    e1.delete(0, "end")

def display():
    e2.config(state="normal")
    e2.insert(0, "hello, " + e1.get())
    e2.config(state="disabled")


root = tk.Tk()
txt = tk.StringVar()
l1 = tk.Label(root, text="enter your name")
e1 = tk.Entry(root, bd=5, textvariable="txt")
e2 = tk.Entry(root, bd=5)
b1 = tk.Button(root, text="clear", command=clear)
b2 = tk.Button(root, text = "display", command=display)



l1.pack()
e1.pack()
e2.pack()
b1.pack()
b2.pack()

e2.config(state = "disabled")

root.mainloop()