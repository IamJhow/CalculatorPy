from tkinter import *
from tkinter import ttk

color1 = "black"
color2 = "white"
color3 = "#333a58"
color4 = "#50556e"
color5 = "#fe3663"
color6 = "#a23b64"

window = Tk()
window.title("Calc")
window.geometry("235x310")
window.config(bg=color1)

framescreen = Frame(window, width=235, height=50, bg=color3)
framescreen.grid(row=0, column=0)

framebody = Frame(window, width=235, height=268)
framebody.grid(row=1, column=0)

allvalues = ''

valuetext = StringVar()

def entervalues(event):

    global allvalues
    allvalues = allvalues + str(event)
    valuetext.set(allvalues)


def calculate():

    global allvalues
    result = eval(allvalues)
    print(result)

    valuetext.set(str(result))

def cleanscreen():

    global allvalues
    allvalues = ""
    valuetext.set("")


applabel = Label(framescreen, textvariable= valuetext, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('MonoSpace 18'), bg=color3, fg=color2)
applabel.place(x=0, y=0)

button1 = Button(framebody, command= cleanscreen, text="C", width=11, height=2, bg=color4, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button1.place(x=0, y=0)
button2 = Button(framebody, command = lambda: entervalues('%'), text="%", width=5, height=2, bg=color4, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button2.place(x=118, y=0)
button3 = Button(framebody, command = lambda: entervalues('/'), text="/", width=5, height=2, bg=color4, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button3.place(x=177, y=0)
button4 = Button(framebody, command = lambda: entervalues('7'), text="7", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button4.place(x=0, y=52)
button5 = Button(framebody, command = lambda: entervalues('8'), text="8", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button5.place(x=59, y=52)
button6 = Button(framebody, command = lambda: entervalues('9'), text="9", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button6.place(x=118, y=52)
button7 = Button(framebody, command = lambda: entervalues('*'), text="*", width=5, height=2, bg=color4, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button7.place(x=177, y=52)
button8 = Button(framebody, command = lambda: entervalues('4'), text="4", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button8.place(x=0, y=104)
button9 = Button(framebody, command = lambda: entervalues('5'), text="5", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button9.place(x=59, y=104)
button10 = Button(framebody, command = lambda: entervalues('6'), text="6", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button10.place(x=118, y=104)
button11 = Button(framebody, command = lambda: entervalues('-'), text="-", width=5, height=2, bg=color4, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button11.place(x=177, y=104)
button12 = Button(framebody, command = lambda: entervalues('1'), text="1", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button12.place(x=0, y=156)
button13 = Button(framebody, command = lambda: entervalues('2'), text="2", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button13.place(x=59, y=156)
button14 = Button(framebody, command = lambda: entervalues('3'), text="3", width=5, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button14.place(x=118, y=156)
button15 = Button(framebody, command = lambda: entervalues('+'), text="+", width=5, height=2, bg=color4, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button15.place(x=177, y=156)
button16 = Button(framebody, command = lambda: entervalues('0'), text="0", width=11, height=2, bg=color3, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button16.place(x=0, y=208)
button17 = Button(framebody, command = lambda: entervalues('.'), text=".", width=5, height=2, bg=color3, fg=color6, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button17.place(x=118, y=208)
button18 = Button(framebody, command = calculate, text="=", width=5, height=2, bg=color5, fg=color2, font=('MonoSpace 13 bold'), relief=RAISED, overrelief=RIDGE)
button18.place(x=177, y=208)

window.mainloop()