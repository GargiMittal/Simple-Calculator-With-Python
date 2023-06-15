
from tkinter import *
def myclick():
    myLabel=Label(root,text="boop!!!")
    myLabel.pack()


root=Tk()
root.title("BOOP!")

myButton=Button(root,text="CLICK ME!!",padx=50,pady=10,command=myclick)
myButton.pack()
root.mainloop()