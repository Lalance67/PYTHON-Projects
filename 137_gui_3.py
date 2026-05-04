import tkinter as tk

root = tk.Tk()
message = tk.Label(root, text="This is an example of a Label", width = 50, height = 25)
message.pack(expand=10)
root.mainloop()