import arcaea_crawler as arc
import tkinter



win = tkinter.Tk()
win.title("Arcaea")
win.geometry("300x300+300+300")

str=tkinter.StringVar()  
warning = tkinter.Label(win, textvariable=str, fg='red', font=('宋体', 10))  
warning.place(x=30, y=120, anchor='nw')


def func():
    str.set(arc.query(variable.get()))

    
variable = tkinter.StringVar()
entry = tkinter.Entry(win,textvariable=variable)
button = tkinter.Button(win,text="查询",width=7,bg="#ffcccc",command=func)


entry.pack()
button.pack()
win.mainloop()

