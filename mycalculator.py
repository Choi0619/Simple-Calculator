from tkinter import *

window = None
displayLabel = None
equation = None
expression = ""

def guiMain():
    setupGUI()
    window.mainloop()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clearDisplay():
    displayLabel['text'] = "0"
    equation.set("0")

def equalPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def setupGUI():
    global window
    global displayLabel
    global equation
    window = Tk()
    window.title("MyCalulator")
    window.configure(background="honeydew")
    equation = StringVar()
    equation.set('enter')


    displayLabel = Label(window, textvariable=equation, relief=SUNKEN, bg = 'white', width=15, font='Arial 20')
    displayLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    btn0 = Button(window, text='0', relief = RAISED, fg= 'black', bg= 'snow',  width=5, height=2, font='Arial 15', command=lambda: press("0"))
    btn1 = Button(window, text='1', relief = RAISED, fg= 'black', bg= 'rosybrown', width=5, height=2, font='Arial 15', command=lambda: press("1"))
    btn2 = Button(window, text='2', relief = RAISED, fg= 'black', bg= 'rosybrown', width=5, height=2, font='Arial 15', command=lambda: press("2"))
    btn3 = Button(window, text='3', relief = RAISED, fg= 'black', bg= 'rosybrown', width=5, height=2, font='Arial 15', command=lambda: press("3"))
    btn4 = Button(window, text='4', relief = RAISED, fg= 'black', bg= 'light grey', width=5, height=2, font='Arial 15', command=lambda: press("4"))
    btn5 = Button(window, text='5', relief = RAISED, fg= 'black', bg= 'light grey', width=5, height=2, font='Arial 15', command=lambda: press("5"))
    btn6 = Button(window, text='6', relief = RAISED, fg= 'black', bg= 'light grey', width=5, height=2, font='Arial 15', command=lambda: press("6"))
    btn7 = Button(window, text='7', relief = RAISED, fg= 'black', width=5, height=2, font='Arial 15', command=lambda: press("7"))
    btn8 = Button(window, text='8', relief = RAISED, fg= 'black', width=5, height=2, font='Arial 15', command=lambda: press("8"))
    btn9 = Button(window, text='9', relief = RAISED, fg= 'black', width=5, height=2, font='Arial 15', command=lambda: press("9"))

    decimalBtn = Button(window, text='.', relief = RAISED, fg= 'white', bg= 'blue', width=5, height=2, font='Arial 15', command=lambda: press("."))
    eraseBtn =   Button(window, text='<', relief = RAISED, fg= 'white', bg= 'orange', width=5, height=1, font='Arial 15', command=lambda: press("[-1]"))
    percentBtn = Button(window, text='%', relief = RAISED, fg= 'white', bg= 'yellow', width=5, height=1, font='Arial 15', command=lambda: len[-1])
    squareBtn =  Button(window, text='X^2', relief = RAISED, fg= 'white', bg= 'green', width=5, height=1, font='Arial 15', command=lambda: press("**2"))
    clearBtn =   Button(window, text='C', relief = RAISED, fg= 'white', bg= 'red', width=5, height=1, font='Arial 15', command=clearDisplay)
    resultBtn =  Button(window, text='=', relief = RAISED, fg= 'white', bg= 'purple', width=5, height=2, font='Arial 15', command=equalPress)
    addBtn =     Button(window, text='+', relief = RAISED, fg= 'brown', bg= 'cornsilk', width=5, height=2, font='Arial 15', command=lambda: press("+"))
    subBtn =     Button(window, text='-', relief = RAISED, fg= 'brown', bg= 'cornsilk', width=5, height=2, font='Arial 15', command=lambda: press("-"))
    mulBtn =     Button(window, text='*', relief = RAISED, fg= 'brown', bg= 'cornsilk', width=5, height=2, font='Arial 15', command=lambda: press("*"))
    divBtn =     Button(window, text='/', relief = RAISED, fg= 'brown', bg= 'cornsilk', width=5, height=2, font='Arial 15', command=lambda: press("/"))

    clearBtn.grid   (row=1, column=0)
    eraseBtn.grid   (row=1, column=1)
    percentBtn.grid (row=1, column=2)
    squareBtn.grid  (row=1, column=3)
    btn1.grid       (row=2, column=0)
    btn2.grid       (row=2, column=1)
    btn3.grid       (row=2, column=2)
    btn4.grid       (row=3, column=0)
    btn5.grid       (row=3, column=1)
    btn6.grid       (row=3, column=2)
    btn7.grid       (row=4, column=0)
    btn8.grid       (row=4, column=1)
    btn9.grid       (row=4, column=2)
    decimalBtn.grid (row=5, column=0)
    btn0.grid       (row=5, column=1)
    resultBtn.grid  (row=5, column=2)
    addBtn.grid     (row=2, column=3)
    subBtn.grid     (row=3, column=3)
    mulBtn.grid     (row=4, column=3)
    divBtn.grid     (row=5, column=3)

guiMain()
