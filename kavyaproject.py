from tkinter import *
import tkinter 

main = Tk()
main.title('Calculator')
frame = Frame(master=main, bg="black",width=50)
frame.pack()

val=""


input=StringVar()

def click(num):
        global val
        val = val + str(num)
        input.set(val)

def equal():
    x=str(eval(inputframe.get()))
    inputframe.delete(0,END)
    inputframe.insert(0,x)   

def clear():
    global val
    val=""
    input.set("")
    




num1 = Button(frame, text='1',width=10,height=3,command=lambda: click(1))
num1.grid(row=1, column=0)
num2 = Button(frame, text='2',width=10,height=3,command=lambda: click(2))
num2.grid(row=1, column=1)
num3 = Button(frame,width=10,height=3, text='3',command=lambda: click(3))
num3.grid(row=1, column=2)
num4 = Button(frame,width=10,height=3, text='4',command=lambda: click(4))
num4.grid(row=2, column=0)
num5 = Button(frame,width=10,height=3, text='5',command=lambda: click(5))
num5.grid(row=2, column=1)
num6 = Button(frame,width=10,height=3, text='6',command=lambda: click(6))
num6.grid(row=2, column=2)
num7 = Button(frame, width=10,height=3,text='7',command=lambda: click(7))
num7.grid(row=3, column=0)
num8 = Button(frame,width=10,height=3,text='8',command=lambda: click(8))
num8.grid(row=3, column=1)
num9 = Button(frame,width=10,height=3, text='9',command=lambda: click(9))
num9.grid(row=3, column=2)
num0 = Button(frame,width=10,height=3, text='0', command=lambda: click(0))
num0.grid(row=4, column=1)

add = Button(frame,width=10,height=3, text="+",command=lambda: click('+'))
add.grid(row=5, column=0)

subtract = Button(
	frame, text="-",width=10,height=3, command=lambda: click('-'))
subtract.grid(row=5, column=1)

multiply = Button(
	frame, text="*",width=10,height=3,command=lambda: click('*'))
multiply.grid(row=5, column=2)

div = Button(frame, text="/",width=10,height=3,command=lambda: click('/'))
div.grid(row=6, column=0)

clearinput = Button(frame, text="clear",width=10,height=3,
					command=clear)
clearinput.grid(row=6, column=1)
equalto = Button(frame, text="=",height=3,
						width=10, command=equal)
equalto.grid(row=6, column=2)

inputframe = Entry(frame,textvariable=input , width=20)
inputframe.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

main.mainloop()
