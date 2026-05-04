# import tkinter as tk

# root = tk.Tk()
# root.title("My first GUI")
# root.geometry("300x200")

# my_label = tk.Label(root, text="Hello, tkinter!", font=("Arial", 16))

# my_label.pack(pady=20)

# root.mainloop()


import tkinter as tk

root = tk.Tk() # to create a window
root.title("My first GUI") # title
root.geometry("300x200") #size

my_label = tk.Label(root, text="Hello, tkinter!", font=("Arial", 16)) # label

my_label.pack(pady=20) # can be pack, grid, place

root.mainloop() # to run