import tkinter
from tkinter import *
import webbrowser
def about_me():
    r = Tk()
    Label(r, text = 'Important link', font =('Verdana', 15)).pack(side = TOP, pady = 10)
    #photo = PhotoImage(file = "l.png")
    #photoimage = photo.subsample(3, 3)
    #Button(r, text = 'Click Me !', image = photoimage,compound = LEFT,command=openlinkedin).pack(side = TOP)
    Button(r, text = 'Linkedin', compound = LEFT,command=openlinkedin).pack(side = TOP)
    mainloop() 
  

def openlinkedin():
    webbrowser.open('https://www.linkedin.com/in/aditya-pa/')
