import tkinter as tk

def change_text():
    message_label.config(text="You clicked the button!")

root = tk.Tk()
root.title("my 2nd gui")
root.geometry("300x200")

message_label = tk.Label(root, text="Waiting for a click", font=("Arial", 15))
action_button = tk.Button(root, text="click me", command=change_text)

message_label.pack(pady=20)
action_button.pack(pady=10)

root.mainloop()