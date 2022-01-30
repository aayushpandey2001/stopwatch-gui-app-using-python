from tkinter import*
t=0


def set_timer():
    global t
    t=t+int(e1.get())
    return t


def countdown():
    global t
    if t>0:
        l1.config(text=t)
        t=t-1
        l1.after(1000,countdown)
    elif t==0:
        print("end")
        l1.config(text="Goo")



root=Tk()
root.title("My StopWatch")
root.geometry("700x700")

l1=Label(root,font="time 20")
l1.grid(row=1,column=2)

times=StringVar()
e1=Entry(root,textvariable=times)
e1.grid(row=3,column=2)

b1=Button(root,text="SET",width=50,command=set_timer)
b1.grid(row=4,column=2,padx=150)

b2=Button(root,text="START",width=50,command=countdown)
b2.grid(row=6,column=2,padx=20)



root.mainloop()