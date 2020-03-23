from tkinter import *
from tkinter import messagebox
import serial
import time
ard=serial.Serial('COM6',9600)
time.sleep(2)

def color(red,green,blue):
    if type(red)==int and type(blue)==int and type(green)==int:
        x='{0}-{1}*{2}'.format(red,green,blue)
        ard.write(bytes(x,'utf8'))
    else:
        messagebox.showerror("Invalid data type",'Enter from range 0-255')

root=Tk()
root.title("Serial")
root.geometry("600x100")


l1=Label(root,text="Enter RGB Values : ").pack()

l1=Label(root,text=" RED : ").pack(side=LEFT)
e1=Entry(root)
e1.pack(side=LEFT)

l2=Label(root,text=" GREEN : ").pack(side=LEFT)
e2=Entry(root)
e2.pack(side=LEFT)

l3=Label(root,text=" BLUE : ").pack(side=LEFT)
e3=Entry(root)
e3.pack(side=LEFT)

b1=Button(root,text="LOAD",command=lambda:color(int(e1.get()),int(e2.get()),int(e3.get())))
b1.pack(side=LEFT,padx=10)
b1.bind("<Return>",color)
root.mainloop()
