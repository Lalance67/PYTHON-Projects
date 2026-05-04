import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")

l1 = tk.Label(root, text = "message box examples", font = "75")
l1.pack()

tk.messagebox.showinfo("showinfo", "info")
# tk.messagebox.showwarning("showwarning", "warning")
# tk.messagebox.showerror("showerror", "error")
# tk.messagebox.askquestion("askquestion", "askquestion")
# tk.messagebox.askokcancel("askokcancel", "cancel")
# tk.messagebox.askyesno("askyesno", "yes or no")
# tk.messagebox.askretrycancel("askretrycancel", "askretrycancel")





