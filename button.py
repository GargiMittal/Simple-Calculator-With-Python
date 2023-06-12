from tkinter import *
def myclick():
    myLabel=Label(root,text="boop!!!")
    myLabel.pack()


root=Tk()
myButton=Button(root,text="CLICK ME!!",padx=50,command=myclick)
myButton.pack()
root.mainloop()