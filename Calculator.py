import customtkinter as ctk

currentText = "0"
num = 0
op = ""

def updateText():
    global currentText
    if len(currentText) == 0:
        currentText = "0"

    if len(currentText) > 12:
        currentText = currentText[:12]

    calcLabel.configure(text=currentText)

def addText(str):
    global currentText
    if float(currentText) == 0 and str != '.' and '.' not in currentText:
        currentText = ""

    if '.' in currentText and str == '.':
        return

    currentText = currentText + str
    updateText()

def CE():
    global currentText
    global num
    global op
    currentText = "0"
    num = 0
    op = ""
    updateText()

def Back():
    global currentText
    currentText = currentText[:len(currentText)-1]
    updateText()

def plus_minus():
    global currentText
    if '-' in currentText:
        currentText = currentText.replace('-', '')
    else:
        currentText = '-' + currentText
    updateText()


if op == '+':
    result= num + currentNum

    num = result
    currentText = str(result)
    updateText()

def calculate():
    global currentText
    global num
    global op

    currentNum = float(currentText)
    result = 0
    if op == '+':
        result = num + currentNum
    num = result
    currentText = str(result)
    updateText()

    if op == '-':
        result = num - currentNum
    num = result1
    currentText = str(result)
    updateText()
def operation(str):
    global currentText
    global num
    global op

    if op == "":
        num = float(currentText)
        currentText = "0"
    else:
        calculate()

    if str == '=':
        op = ""
    else:
        op = str
        currentText = "0"


app = ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
app.configure(bg_color="white", fg_color="white")

calcFrame = ctk.CTkFrame(master=app, width=340, height=90,
                         bg_color="white", fg_color="white")
calcFrame.grid(row=0, column=0, padx=5, pady=5)

calcLabel = ctk.CTkLabel(master=calcFrame, text="0", width=330, height=80,
                         anchor="e", font=ctk.CTkFont(size=50),
                         bg_color="white", fg_color="white")
calcLabel.grid(row=0, column=0, padx=5)


btnFrame = ctk.CTkFrame(master=app, width=340, height=400,
                        bg_color="white", fg_color="white")
btnFrame.grid(row=1, column=0, padx=5, pady=5)

# row = 0
btnCE = ctk.CTkButton(master=btnFrame, text="CE", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white", command=CE)
btnCE.grid(row=0, column=0, padx=2, pady=2)

btnBack = ctk.CTkButton(master=btnFrame, text="<--", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white", command=Back)
btnBack.grid(row=0, column=1, padx=2, pady=2)

btnPercent = ctk.CTkButton(master=btnFrame, text="%", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnPercent.grid(row=0, column=2, padx=2, pady=2)

btnDivide = ctk.CTkButton(master=btnFrame, text="/", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnDivide.grid(row=0, column=3, padx=2, pady=2)

# row = 1
btn7 = ctk.CTkButton(master=btnFrame, text="7", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("7"))

btn7.grid(row=1, column=0, padx=2, pady=2)

btn8 = ctk.CTkButton(master=btnFrame, text="8", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("8"))
btn8.grid(row=1, column=1, padx=2, pady=2)

btn9 = ctk.CTkButton(master=btnFrame, text="9", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("9"))
btn9.grid(row=1, column=2, padx=2, pady=2)

btnMultiply = ctk.CTkButton(master=btnFrame, text="X", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnMultiply.grid(row=1, column=3, padx=2, pady=2)

# row = 2
btn4 = ctk.CTkButton(master=btnFrame, text="4", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("4"))
btn4.grid(row=2, column=0, padx=2, pady=2)

btn5 = ctk.CTkButton(master=btnFrame, text="5", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("5"))
btn5.grid(row=2, column=1, padx=2, pady=2)

btn6 = ctk.CTkButton(master=btnFrame, text="6", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("6"))
btn6.grid(row=2, column=2, padx=2, pady=2)

btnSubstract = ctk.CTkButton(master=btnFrame, text="-", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white", command=lambda: operation('minus'))
btnSubstract.grid(row=2, column=3, padx=2, pady=2)

# row = 3
btn1 = ctk.CTkButton(master=btnFrame, text="1", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("1"))
btn1.grid(row=3, column=0, padx=2, pady=2)

btn2 = ctk.CTkButton(master=btnFrame, text="2", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("2"))
btn2.grid(row=3, column=1, padx=2, pady=2)

btn3 = ctk.CTkButton(master=btnFrame, text="3", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("3"))
btn3.grid(row=3, column=2, padx=2, pady=2)

btnAdd = ctk.CTkButton(master=btnFrame, text="+", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white", command=lambda: operation('+'))
btnAdd.grid(row=3, column=3, padx=2, pady=2)

# row = 4
btnPlus_minus = ctk.CTkButton(master=btnFrame, text="+/-", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white", command=plus_minus)
btnPlus_minus.grid(row=4, column=0, padx=2, pady=2)

btn0 = ctk.CTkButton(master=btnFrame, text="0", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("0"))
btn0.grid(row=4, column=1, padx=2, pady=2)

btnDot = ctk.CTkButton(master=btnFrame, text=".", width=75, height=65,
                      font=ctk.CTkFont(size=30), text_color="black",
                      fg_color="gray75", bg_color="white",
                       command=lambda : addText("."))
btnDot.grid(row=4, column=2, padx=2, pady=2)

btnEqual = ctk.CTkButton(master=btnFrame, text="=", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white", command=lambda: operation('-'))
btnEqual.grid(row=4, column=3, padx=2, pady=2)

app.mainloop()