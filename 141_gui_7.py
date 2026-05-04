from tkinter import *
from tkinter import messagebox
frame = Tk()

def Clear():
    # Ask the user for confirmation before clearing
    response = messagebox.askquestion("Confirm Clear", "Are you sure you want to clear the entries?")
    
    # If the user clicks 'yes', proceed with clearing
    if response == 'yes':
        E1.delete(0,END)
        E2.config(state=NORMAL)
        E2.delete(0,END)
        E2.config(state=DISABLED)

def Display():
    E2.config(state=NORMAL)
    E2.insert(0,"Hello " + E1.get())
    E2.config(state=DISABLED)

# widgets declarations
L1 = Label(frame, text="Enter your name: ")
E1 = Entry(frame, bd=5)
E2 = Entry(frame, bd=5)
B1 = Button(frame, text="CLEAR", command=Clear)
B2 = Button(frame, text="DISPLAY", command=Display)      

# adding widgets
L1.pack()
E1.pack()
E2.pack()
B1.pack()
B2.pack()

#initializing widgets
E2.config(state=DISABLED)
frame.mainloop()