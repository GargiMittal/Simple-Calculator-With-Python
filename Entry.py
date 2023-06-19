from tkinter import *

root=Tk()
root.title("Hi User")
myLabel1=Label(root,text="Enter Your Name here: ")
myLabel1.pack()

e=Entry(root,width=40,borderwidth=5)
e.pack()
e.insert(1,"i.e, Neha")

def myclick():
#test
    name=e.get()
    myLabel=Label(root,text="Hi!! "+name)
    myLabel.pack()

myButton=Button(root,text="Enter",command=myclick)
myButton.pack()

root.mainloop()