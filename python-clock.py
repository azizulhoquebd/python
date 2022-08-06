#
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.resizable(0,0)
root.geometry("950×200")
root["bg"]="black"
root.title("clock")

label=Label(root,font=("ds_digital",150),background="black",foreground="cyan")
label.pack(anchor="center")

mainloop()
