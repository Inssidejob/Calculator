from tkinter import *
expression=""
def press(num):
    global expression
    expression+=str(num)
    equation.set(expression)
def erase():
    global expression
    expression=""
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
root=Tk()
root.title("CHIRAYU CALCULATOR")
root.configure(background="light green")
root.geometry("270x250")
equation=StringVar()
Expression=Entry(root,textvariable=equation)
Expression.grid(columnspan=4,ipadx=70)
b1=Button(root,text=9,fg="black",command=lambda:press(9),height=1,width=7,borderwidth=4)
b1.grid(row=2,column=0)
b2=Button(root,text=8,fg="black",command=lambda:press(8),height=1,width=7,borderwidth=4)
b2.grid(row=2,column=1)
b3=Button(root,text=7,fg="black",command=lambda:press(7),height=1,width=7,borderwidth=4)
b3.grid(row=2,column=2)
b4=Button(root,text=6,command=lambda:press(6),height=1,width=7,borderwidth=4)
b4.grid(row=3,column=0,pady=8)
b5=Button(root,text=5,fg="black",command=lambda:press(5),height=1,width=7,borderwidth=4)
b5.grid(row=3,column=1,pady=8)
b6=Button(root,text=4,fg="black",command=lambda:press(4),height=1,width=7,borderwidth=4)
b6.grid(row=3,column=2,pady=8)
b7=Button(root,text=3,fg="black",command=lambda:press(3),height=1,width=7,borderwidth=4)
b7.grid(row=4,column=0,pady=4)
b8=Button(root,text=2,fg="black",command=lambda:press(2),height=1,width=7,borderwidth=4)
b8.grid(row=4,column=1,pady=4)
b9=Button(root,text=1,fg="black",command=lambda:press(1),height=1,width=7,borderwidth=4)
b9.grid(row=4,column=2,pady=4)
b10=Button(root,text='Clear',command=erase,fg="black",borderwidth=4,height=1,width=7)
b10.grid(row=5,column=0,pady=6)
b11=Button(root,text="+",fg="black",command=lambda:press('+'),height=1,width=7,borderwidth=4)
b11.grid(row=5,column=1,pady=6)
b12=Button(root,text="-",fg="black",command=lambda:press('-'),height=1,width=7,borderwidth=4)
b12.grid(row=5,column=2,pady=6)
b13=Button(root,text="*",command=lambda:press("*"),height=1,width=7,borderwidth=4,pady=8)
b13.grid(row=6,column=0,pady=8)
b14=Button(root,text="/",fg="black",command=lambda:press("/"),height=1,width=7,borderwidth=4,pady=8)
b14.grid(row=6,column=1,pady=8)
b15=Button(root,text="=",fg="black",command=equalpress,height=1,width=7,pady=8,borderwidth=4)
b15.grid(row=6,column=2,pady=8)
root.mainloop()