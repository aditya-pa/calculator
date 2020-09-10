import tkinter
from tkinter import *
import webbrowser
def about_me():
    r = Tk()
    r.geometry("300x200")
    frame_0=Frame(r)
    frame_0.pack(expand = True,fill = 'both')
    frame_1=Frame(r)
    frame_1.pack(expand = True,fill = 'both')
    frame_2=Frame(r )
    frame_2.pack(expand = True,fill = 'both')
    Label(frame_0, text = 'Important link', font =('Verdana', 15)).pack(side = TOP, pady = 10)
    Button(frame_1, text = 'Linkedin', relief='groove',compound = LEFT,command=openlinkedin,font = ('verdana',22)).pack(side='left',expand=True,fill='both')
    Button(frame_2, text = 'Github',  relief='groove',compound = LEFT,command=github,font = ('verdana',22)).pack(side='left',expand=True,fill='both',)
    mainloop() 
  
def openlinkedin():
    webbrowser.open('https://www.linkedin.com/in/aditya-pa/')
def github():
    webbrowser.open('https://github.com/aditya-pa/calculator')

