import tkinter
from tkinter import *
import about
root=tkinter.Tk()
var=''
hist=''
photo1=PhotoImage(file = 'A2.png')
p2=PhotoImage(file = 'mode.png')
photo2 = p2.subsample(4,4)

img1=photo1
img2=photo2
BR="#d3d3d3"
FR="#000000"
DBR="#FFFFFF"
DFR="#000000"
HBR="#849ae3"
HFR="#ffffff"
sub="#ffffff"
B=0
flag=False
f=True

def change():
    global flag
    global BR
    global FR
    global DBR
    global DFR
    global HBR
    global HFR
    if flag:
        BR="#d3d3d3"
        FR="#000000"
        DBR="#FFFFFF"
        DFR="#000000"
        HBR="#849ae3"
        HFR="#ffffff"
        invert_colours()
        flag=False
    else:
        BR="#000000"
        FR="#b5b3b3"
        DBR="#383737"
        DFR="#808080"
        HBR="#c7c1c1"
        HFR="#ffffff"
        invert_colours()
        flag=True

def invert_colours():
    root.config(bg=DBR)
    mainmenu1.config(background=DBR,activebackground=HBR) 
    submenu1.config(background=DBR,foreground=FR, activebackground=HBR,activeforeground=HFR)   
     
    button_1.config(
    background = BR,
    fg = FR,
    border=B)
    button_2.config(
    background = BR,
    fg = FR,
    border=B)
    button_3.config(
    background = BR,
    fg = FR,
    border=B)
    button_4.config(
    background = BR,
    fg = FR,
    border=B)
    button_5.config(
    background = BR,
    fg = FR,
    border=B)
    button_6.config(
    background = BR,
    fg = FR,
    border=B)
    button_7.config(
    background = BR,
    fg = FR,
    border=B)
    button_8.config(
    background = BR,
    fg = FR,
    border=B)
    button_9.config(
    background = BR,
    fg = FR,
    border=B)
    button_0.config(
    background = BR,
    fg = FR,
    border=B)
    button_.config(
    background = BR,
    fg = FR,
    border=B)
    button_plus.config(
    background = BR,
    fg = FR,
    border=B)
    button_minus.config(
    background = BR,
    fg = FR,
    border=B)
    button_photo.config(
    background = BR,
    fg = FR,
    image=img1,
    border=B)
    button_photo2.config(
    background = BR,
    fg = FR,
    image=img2,
    border=B)
    button_square.config(
    background = BR,
    fg = FR,
    border=B)
    button_mul.config(
    background = BR,
    fg = FR,
    border=B)
    button_e.config(
    background = BR,
    fg = FR,
    border=B)
    button_c.config(
    background = BR,
    fg = FR,
    border=B)
    button_pm.config(
    background = BR,
    fg = FR,
    border=B)
    button_p.config(
    background = BR,
    fg = FR,
    border=B)
    button_u.config(
    background = BR,
    fg = FR,
    border=B)
    button_div.config(
    background = BR,
    fg = FR,
    border=B)
    entry_1.config(
    background = DBR,
    fg = DFR,)
    label_2.config(
    background = DBR,
    fg = DFR,)
    label.config(
    background = DBR,
    fg = DFR,)
def destroy():
    root.destroy()

def entered1(event):
    button_1.config(
        background = HBR,
        fg = HFR,)


def leave1(event):
    button_1.config(
        background = BR,
        fg = FR,)


def entered2(event):
    button_2.config(
        background = HBR,
        fg = HFR)


def leave2(event):
    button_2.config(
        background = BR,
        fg = FR)


def entered3(event):
    button_3.config(
        background = HBR,
        fg = HFR)


def leave3(event):
    button_3.config(
        background = BR,
        fg = FR)

def entered4(event):
    button_4.config(
        background = HBR,
        fg = HFR)


def leave4(event):
    button_4.config(
        background = BR,
        fg = FR)


def entered5(event):
    button_5.config(
        background = HBR,
        fg = HFR)
        


def leave5(event):
    button_5.config(
        background = BR,
        fg = FR)


def entered6(event):
    button_6.config(
        background = HBR,
        fg = HFR)
        

def leave6(event):
    button_6.config(
        background = BR,
        fg = FR)
        

def entered7(event):
    button_7.config(
        background = HBR,
        fg = HFR)
        

def leave7(event):
    button_7.config(
        background = BR,
        fg = FR)
def entered8(event):
    button_8.config(
        background = HBR,
        fg = HFR)
def leave8(event):
    button_8.config(
        background = BR,
        fg = FR)
def entered9(event):
    button_9.config(
        background = HBR,
        fg = HFR)
def leave9(event):
    button_9.config(
        background = BR,
        fg = FR)
def entered0(event):
    button_0.config(
        background = HBR,
        fg = HFR)
def leave0(event):
    button_0.config(
        background = BR,
        fg = FR)
def entered_(event):
    button_.config(
        background = HBR,
        fg = HFR)
def leave_(event):
    button_.config(
        background = BR,
        fg = FR)
def enteredplus(event):
    button_plus.config(
        background = HBR,
        fg = HFR)
def leaveplus(event):
    button_plus.config(
        background = BR,
        fg = FR)
def enteredminus(event):
    button_minus.config(
        background = HBR,
        fg = HFR)
def leaveminus(event):
    button_minus.config(
        background = BR,
        fg = FR)
def enteredphoto(event):
    button_photo.config(
        background = HBR,)
def leavephoto(event):
    button_photo.config(
        background = BR,)
def enteredphoto2(event):
    button_photo2.config(
        background = HBR,)
def leavephoto2(event):
    button_photo2.config(
        background = BR,)
def enteredsquare(event):
    button_square.config(
        background = HBR,
        fg = HFR)
def leavesquare(event):
    button_square.config(
        background = BR,
        fg = FR)
def enteredmul(event):
    button_mul.config(
        background = HBR,
        fg = HFR)
def leavemul(event):
    button_mul.config(
        background = BR,
        fg = FR)
def enterede(event):
    button_e.config(
        background = HBR,
        fg = HFR)
def leavee(event):
        button_e.config(
        background = BR,
        fg = FR)
def enteredc(event):
    button_c.config(
        background = HBR,
        fg = HFR)
def leavec(event):
    button_c.config(
        background = BR,
        fg = FR)
def enteredpm(event):
    button_pm.config(
        background = HBR,
        fg = HFR)
def leavepm(event):
    button_pm.config(
        background = BR,
        fg = FR)
def enteredp(event):
    button_p.config(
        background = HBR,
        fg = HFR)
def leavep(event):
    button_p.config(
        background = BR,
        fg = FR)
def enteredu(event):
    button_u.config(
        background = HBR,
        fg = HFR)
def leaveu(event):
    button_u.config(
        background = BR,
        fg = FR)
def entereddiv(event):
    button_div.config(
        background = HBR,
        fg = HFR)
def leavediv(event):
    button_div.config(
        background = BR,
        fg = FR)
def clicked1(v):
    global var
    if len(var) > 1:
        if (var[-1] == "." or var[-1] == ")" or var[-1] == "*" or var[-1] == "-" or var[-1] == "/" or var[-1] == "+" or var[-1] == "**" or var[-1] == "**2" or var[-1] == "**0.5") and v == '.':
            pass


        elif var[-1] == "+":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "+":
                pass
            else:
                var=var + v
        elif var[-1] == "-":
            if v == '+':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "-":
                pass
            else:
                var=var + v



        elif var[-1] == "*":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "*":
                pass
            else:
                var=var + v

        elif var[-1] == "/":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "/":
                pass
            else:
                var=var + v



        else:
            var=var + v
    else:
        var=var + v
    data.set(var)
def clicked(v):
    global var
    if len(var) == 1 and var[0] == "0":
        if v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**":
            var=var + v
        else:
            var=v
        data.set(var)
    elif len(var) == 0:
        if v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**":
            var=var + "0" + v
        else:
            var=var + v
    elif var == '(-0)':
        if not (v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**"):
            var="(-" + v + ")"
        else:
            var=var + v
    elif var[0:2] == '(-' and var[-1] == ')':
        if not (v == '.' or v == '+' or v == '-' or v == '*' or v == '/' or v == "**2" or v == '**0.5' or v == "**"):
            var=var[:-1] + v + ")"

        else:
            var=var + v

    elif len(var) > 5 and var[-5:] == '**0.5':
        if var[-5:] == "**0.5":
            if v == '+':
                var=var[:-5]
                var=var + v
            elif v == '*':
                var=var[:-5]
                var=var + v
            elif v == '/':
                var=var[:-5]
                var=var + v
            elif v == '-':
                var=var[:-5]
                var=var + v
            elif v == "**":
                var=var[:-5]
                var=var + v

            elif v == "**2":
                var=var[:-5]
                var=var + v
            elif v == "**0.5":
                pass
            else:
                var=var + v
        else:
            clicked1(v)

    elif len(var) > 3 and var[-3:] == '**2':
        if var[-3:] == "**2":
            if v == '+':
                var=var[:-3]
                var=var + v
            elif v == '*':
                var=var[:-3]
                var=var + v
            elif v == '/':
                var=var[:-3]
                var=var + v
            elif v == '-':
                var=var[:-3]
                var=var + v
            elif v == "**":
                var=var[:-3]
                var=var + v
            elif v == "**0.5":
                var=var[:-3]
                var=var + v
            elif v == "**2":
                pass
            else:
                var=var + v
        else:
            clicked1(v)

    elif len(var) > 2 and var[-2:] == '**':
        if var[-2:] == "**":

            if v == '+':
                var=var[:-2]
                var=var + v
            elif v == '*':
                var=var[:-2]
                var=var + v
            elif v == '/':
                var=var[:-2]
                var=var + v
            elif v == '-':
                var=var[:-2]
            elif v == "**0.5":
                var=var[:-2]
                var=var + v
            elif v == "**2":
                var=var[:-2]
                var=var + v
            elif v == "**":
                pass
            else:
                var=var + v
        else:
            clicked1(v)

    elif len(var) == 2 and var[1] == "0" and var[0] == "-":
        var="(-" + v + ")"


    elif len(var) > 1:
        if (var[-1] == "." or var[-1] == ")" or var[-1] == "*" or var[-1] == "-" or var[-1] == "/" or var[-1] == "+" or var[-1] == "**" or var[-1] == "**2" or var[-1] == "**0.5") and v == '.':
            pass
        elif var[-1] == "+":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "+":
                pass
            else:
                var=var + v
        elif var[-1] == "-":
            if v == '+':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "-":
                pass
            else:
                var=var + v



        elif var[-1] == "*":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == '/':
                var=var[:-1]
                var=var + v
            elif v == "*":
                pass
            else:
                var=var + v

        elif var[-1] == "/":
            if v == '-':
                var=var[:-1]
                var=var + v
            elif v == '*':
                var=var[:-1]
                var=var + v
            elif v == '+':
                var=var[:-1]
                var=var + v
            elif v == "**":
                var=var[:-1]
                var=var + v
            elif v == "**0.5":
                var=var[:-1]
                var=var + v
            elif v == "**2":
                var=var[:-1]
                var=var + v
            elif v == "/":
                pass
            else:
                var=var + v
        else:
            var=var + v
    else:
        var=var + v
    data.set(var)
def pm():
    global var
    if len(var) == 0:
        var="(-0)"
    elif (var[0:2] == '-(' or var [0:2]=='(-')and var[-1] == ')':
        var=var[2:]
        var=var[:-1]
    else:
        var="-(" + var + ")"
    data.set(var)   
def delete():
    global var
    try:
        if var[-1]==')':
            for i,j in enumerate(var):
                if j=='(':
                    var=var[:i]+var[i+1:]


        var=var[:-1]
        data.set(var)
    except:
        pass
        
def c():
    global var
    global hist
    try:
        if var=='':
            hist=''
            label.config(text=hist)
        else:
            var=""
            data.set(var)
    except:
        pass
def solve():
    global var
    global hist
    try:
        hist=var
        label.config(text=hist)
        ans=eval(var)            
        ans=round(ans,4)
        var=str(ans)
            
        if var[0] == "-":
            var="(" + var + ")"
        data.set(var)
        
    except ZeroDivisionError:
        data.set("Can't Divide by Zero")
    except SyntaxError:
        data.set("Syntax Error")
    except:
        data.set("Invalid Input")
def enterpress(event):
    solve()
def click(event):
    clicked(event.char)
def deleteclick(event):
    c()
def backspace(event):
    delete()
def resize():
    global f
    global root
    if f:
        root.resizable(1,1)
        f=False
    else:
        root.resizable(0,0)
        f=True

def clicked_history(event):
    global hist
    global var
    data.set(hist)
    var=hist
    hist=""
    label.config(text=hist)
    
root.geometry("300x520")
root.resizable(0,0)
root.title("Calculator")
icon=PhotoImage(file = "calculator.png")
root.tk.call('wm','iconphoto',root._w,icon)
root.config(bg=DBR)
root.bind('0',click)
root.bind('<Return>',enterpress)
root.bind('1',click)
root.bind('2',click)
root.bind('3',click)
root.bind('4',click)
root.bind('5',click)
root.bind('6',click)
root.bind('7',click)
root.bind('8',click)
root.bind('9',click)
root.bind('.',click)
root.bind('*',click)
root.bind('+',click)
root.bind('-',click)
root.bind('/',click)
root.bind('<Delete>',deleteclick)
root.bind('<BackSpace>',backspace)  


imgvar1 = PhotoImage(file='menu.png')
image = imgvar1.subsample(15,20)
mainmenu1 = Menubutton(root, image=image ,background=DBR,activebackground=HBR)
mainmenu1.pack(expand=False,fill=None,anchor=S+W,)
submenu1 = Menu(mainmenu1,tearoff = 0,background=DBR,
foreground=FR, activebackground=HBR,activeforeground=HFR)
mainmenu1.config(menu=submenu1,)
submenu1.add_command(label="DAY/NIGHT",command=change)
submenu1.add_command(label="RESIZE or NOT",command=resize)
submenu1.add_command(label="About",command=about.about_me)
submenu1.add_separator()
submenu1.add_command(label="Quit",command=destroy)


data=StringVar()
data.set(var)
frame_x=Frame(root)
frame_x.pack(side="top",expand=True,fill='both')
frame_1=Frame(root)
frame_1.pack(expand = True,fill = 'both')
frame_2=Frame(root)
frame_2.pack(expand = True,fill = 'both')
frame_3=Frame(root)
frame_3.pack(expand = True,fill = 'both')
frame_4=Frame(root)
frame_4.pack(expand = True,fill = 'both')
frame_5=Frame(root)
frame_5.pack(expand = True,fill = 'both')
frame_6=Frame(root)
frame_6.pack(expand = True,fill = 'both')
frame_7=Frame(root)
frame_7.pack(expand = True,fill = 'both')
label_2=Label(frame_1,background=DBR)
label_2.pack(expand = True,fill = 'both')
label=Label(frame_x,background=DBR,text = hist,font = ('verdana',22),anchor = 'se')
label.bind('<Button-1>',clicked_history)
label.pack(expand = True,fill = 'both')
entry_1=Label(frame_1,
              textvariable = data,
              font = ('verdana',22),
              background = DBR,
              anchor = 'se',
              border = 0,
              fg = DFR)
entry_1.pack(expand = True,fill = 'both')
button_1=Button(
    frame_2,
    command = lambda:clicked("1"),
    text = '1',
    border = B,
    relief = 'groove',
    background = BR,
    fg = FR,
    font = ('verdana',22))
button_1.pack(side = 'left',expand = True,fill = 'both')
button_1.bind('<Enter>',entered1)
button_1.bind('<Leave>',leave1)
button_2=Button(
    frame_2,
    command = lambda:clicked("2"),
    border = B,
    background = BR,
    fg = FR,
    text = '2',
    relief = 'groove',
    font = ('verdana',22))
button_2.pack(side = 'left',expand = True,fill = 'both')
button_2.bind('<Enter>',entered2)
button_2.bind('<Leave>',leave2)
button_3=Button(
    frame_2,
    command = lambda:clicked("3"),
    border = B,
    background = BR,
    fg = FR,
    text = '3',
    relief = 'groove',
    font = ('verdana',22))
button_3.pack(side = 'left',expand = True,fill = 'both')
button_3.bind('<Enter>',entered3)
button_3.bind('<Leave>',leave3)
button_4=Button(
    frame_2,
    command = lambda:clicked("4"),
    border = B,
    background = BR,
    fg = FR,
    text = '4',
    relief = 'groove',
    font = ('verdana',22))
button_4.pack(side = 'left',expand = True,fill = 'both')
button_4.bind('<Enter>',entered4)
button_4.bind('<Leave>',leave4)

button_5=Button(
    frame_3,
    command = lambda:clicked("5"),
    border = B,
    background = BR,
    fg = FR,
    text = '5',
    relief = 'groove',
    font = ('verdana',22))
button_5.pack(side = 'left',expand = True,fill = 'both')
button_5.bind('<Enter>',entered5)
button_5.bind('<Leave>',leave5)
button_6=Button(
    frame_3,
    command = lambda:clicked("6"),
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    text = '6',
    font = ('verdana',22))
button_6.pack(side = 'left',expand = True,fill = 'both')
button_6.bind('<Enter>',entered6)
button_6.bind('<Leave>',leave6)
button_7=Button(
    frame_3,
    command = lambda:clicked("7"),
    relief = 'groove',
    text = '7',
    border = B,
    background = BR,
    fg = FR,
    font = ('verdana',22))
button_7.pack(side = 'left',expand = True,fill = 'both')
button_7.bind('<Enter>',entered7)
button_7.bind('<Leave>',leave7)
button_8=Button(
    frame_3,
    command = lambda:clicked("8"),
    relief = 'groove',
    text = '8',
    border = B,
    background = BR,
    fg = FR,
    font = ('verdana',22))
button_8.pack(side = 'left',expand = True,fill = 'both')
button_8.bind('<Enter>',entered8)
button_8.bind('<Leave>',leave8)

button_9=Button(
    frame_4,
    command = lambda:clicked("9"),
    text = '9',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',

    font = ('verdana',22))
button_9.pack(side = 'left',expand = True,fill = 'both')
button_9.bind('<Enter>',entered9)
button_9.bind('<Leave>',leave9)
button_0=Button(
    frame_4,
    command = lambda:clicked("0"),
    text = '0',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',22))
button_0.pack(side = 'left',expand = True,fill = 'both')
button_0.bind('<Enter>',entered0)
button_0.bind('<Leave>',leave0)
button_=Button(
    frame_4,
    command = lambda:clicked("."),
    text = '.',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',25))
button_.pack(side = 'left',expand = True,fill = 'both')
button_.bind('<Enter>',entered_)
button_.bind('<Leave>',leave_)
button_pm=Button(
    frame_4,
    command = lambda:pm(),
    text = '±',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',19))
button_pm.pack(side = 'left',expand = True,fill = 'both')
button_pm.bind('<Enter>',enteredpm)
button_pm.bind('<Leave>',leavepm)

button_p=Button(
    frame_6,
    command = lambda:clicked("**"),
    border = B,
    background = BR,
    fg = FR,
    text = '^',
    relief = 'groove',
    font = ('verdana',28))
button_p.pack(side = 'left',expand = True,fill = 'both')
button_p.bind('<Enter>',enteredp)
button_p.bind('<Leave>',leavep)
button_u=Button(
    frame_6,
    command = lambda:clicked("**0.5"),
    text = '√x',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_u.pack(side = 'left',expand = True,fill = 'both')
button_u.bind('<Enter>',enteredu)
button_u.bind('<Leave>',leaveu)
button_square=Button(
    frame_6,
    command = lambda:clicked("**2"),
    text = 'x²',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',23))
button_square.pack(side = 'left',expand = True,fill = 'both')
button_square.bind('<Enter>',enteredsquare)
button_square.bind('<Leave>',leavesquare)

button_photo=Button(
    frame_6,
    border = B,
    background = BR,
    fg = FR,
    command = delete,
    image = img1,
    
    relief = 'groove',
    font = ('verdana',22),
    width = 58)
button_photo.pack(side = 'left',expand = True,fill = 'both')
button_photo.bind('<Enter>',enteredphoto)
button_photo.bind('<Leave>',leavephoto)

button_plus=Button(
    frame_5,
    command = lambda:clicked("+"),
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    text = '+',
    font = ('verdana',18))
button_plus.pack(side = 'left',expand = True,fill = 'both')
button_plus.bind('<Enter>',enteredplus)
button_plus.bind('<Leave>',leaveplus)
button_minus=Button(
    frame_5,
    command = lambda:clicked("-"),
    text = '-',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',23))
button_minus.pack(side = 'left',expand = True,fill = 'both')
button_minus.bind('<Enter>',enteredminus)
button_minus.bind('<Leave>',leaveminus)
button_mul=Button(
    frame_5,
    command = lambda:clicked("*"),
    text = '*',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',20))
button_mul.pack(side = 'left',expand = True,fill = 'both')
button_mul.bind('<Enter>',enteredmul)
button_mul.bind('<Leave>',leavemul)
button_div=Button(
    frame_5,
    command = lambda:clicked("/"),
    text = '/',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',23))
button_div.pack(side = 'left',expand = True,fill = 'both')
button_div.bind('<Enter>',entereddiv)
button_div.bind('<Leave>',leavediv)
button_e=Button(
    frame_7,
    command = lambda:solve(),
    text = '=',
    font = ('verdana',22),
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    width = 7)
button_e.pack(side = 'left',expand = True,fill = 'both')
button_e.bind('<Enter>',enterede)
button_e.bind('<Leave>',leavee)
button_photo2=Button(
    frame_7,
    border = B,
    background = BR,
    fg = FR,
    command = change,
    image = img2,
    relief = 'groove',
    font = ('verdana',22),
    width = 55)
button_photo2.pack(side = 'left',expand = True,fill = 'both')
button_photo2.bind('<Enter>',enteredphoto2)
button_photo2.bind('<Leave>',leavephoto2)

button_c=Button(
    frame_7,
    command = lambda:c(),
    text = 'C',
    border = B,
    background = BR,
    fg = FR,
    relief = 'groove',
    font = ('verdana',28))
button_c.pack(side = 'left',expand = True,fill = 'both')
button_c.bind('<Enter>',enteredc)
button_c.bind('<Leave>',leavec)
root.mainloop()

    
