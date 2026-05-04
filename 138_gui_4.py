import tkinter as tk

root = tk.Tk()
l1 = tk.Label(root, text="Enter your name: ", height = 5) # text
l1.pack(side = "left")
e2 = tk.Entry(root, bd = 10) # input text
e2.pack(side = "right")

root.mainloop()