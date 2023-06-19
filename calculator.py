from tkinter import *
root=Tk()
root.title("Calculator")


e=Entry(root,width=44,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    

def button_clear():
    e.delete(0,END)

def button_Add():
    num1=e.get()
    global f_num
    f_num =int(num1)
    e.delete(0,END)
   

def button_equal():
    num2=e.get()
    e.delete(0,END)
    e.insert(0,(f_num+int(num2)))
    

#defining Buttons
button1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_Add=Button(root,text="+",padx=39,pady=20,command= button_Add)
button_Clear=Button(root,text="Clear",padx=81,pady=20,command=button_clear)
button_Equal=Button(root,text="=",padx=91,pady=20,command=button_equal)

#putting buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)


button_Clear.grid(row=5,column=1,columnspan=2)
button_Add.grid(row=5,column=0)
button_Equal.grid(row=4,column=1,columnspan=2)

root.mainloop()