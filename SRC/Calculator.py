import tkinter as tk
from tkinter import ttk
import math
#from ttkthemes import ThemedTk

class Calc(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title('Calculator')
        s = ttk.Style()
        s.theme_use('clam')  #('clam', 'alt', 'default', 'classic')

        BUTTON_PAD = 2
        BUTTON_WIDTH = 5

        self.Display = ttk.Label(self, text="0", justify='center', anchor = tk.E,
                                      background="white", font="-family {DejaVu Sans} -size 18")
        self.Display.grid(row=0, column=0, columnspan=5, pady=5, padx=5, sticky=tk.N+tk.E+tk.W+tk.S)


        def makebutton(label, function, row, col, padx=BUTTON_PAD, pady=BUTTON_PAD, rowspan=1):
            btn = ttk.Button(self, text=label, width=BUTTON_WIDTH, command=function)
            btn.grid(row=row, column=col, pady=pady, padx=padx, rowspan=rowspan, sticky=tk.N + tk.E + tk.W + tk.S)
            return btn

        self.btn7 = makebutton(label="7", function=lambda: self.numberpressed("7"), row=2, col=0)
        self.btn8 = makebutton(label="8", function=lambda: self.numberpressed("8"), row=2, col=1)
        self.btn9 = makebutton(label="9", function=lambda: self.numberpressed("9"), row=2, col=2)
        self.btn4 = makebutton(label="4", function=lambda: self.numberpressed("4"), row=3, col=0)
        self.btn5 = makebutton(label="5", function=lambda: self.numberpressed("5"), row=3, col=1)
        self.btn6 = makebutton(label="6", function=lambda: self.numberpressed("6"), row=3, col=2)
        self.btn1 = makebutton(label="1", function=lambda: self.numberpressed("1"), row=4, col=0)
        self.btn2 = makebutton(label="2", function=lambda: self.numberpressed("2"), row=4, col=1)
        self.btn3 = makebutton(label="3", function=lambda: self.numberpressed("3"), row=4, col=2)
        self.btn0 = makebutton(label="0", function=lambda: self.numberpressed("0"), row=5, col=0)
        self.btndot = makebutton(label=".", function=lambda: self.numberpressed("."), row=5, col=1)
        self.btnsign = makebutton(label="+-", function=lambda: self.numberpressed("+-"), row=5, col=2)
        self.btndiv = makebutton(label='/', function=lambda: self.operationpressed('/'),row=2, col=3, padx=BUTTON_PAD+4)
        self.btnmult = makebutton(label='*', function=lambda: self.operationpressed("*"),row=3, col=3, padx=BUTTON_PAD+4)
        self.btnsub = makebutton(label='-', function=lambda: self.operationpressed("-"),row=4, col=3, padx=BUTTON_PAD+4)
        self.btnadd = makebutton(label='+', function=lambda: self.operationpressed("+"),row=5, col=3, padx=BUTTON_PAD+4)
        self.btnsqr = makebutton(label='√', function=self.sqrootpressed,row=2, col=4, padx=2)
        self.btnpwr = makebutton(label='^', function=lambda: self.operationpressed("^"),row=3, col=4, padx=2)
        self.btneq = makebutton(label='=', function=self.equalpressed,row=4, col=4, padx=2, rowspan=2)
        self.btnback = makebutton(label='DEL', function=self.backspace,row=1, col=2, pady=BUTTON_PAD + 4, padx=0)
        self.btnclear = makebutton(label='C', function=lambda: self.clear("C"),row=1, col=3, pady=BUTTON_PAD+4,padx=BUTTON_PAD+4)
        self.btnce = makebutton(label='CE', function=lambda: self.clear("CE"),row=1, col=4, pady=BUTTON_PAD+4,padx=2)

        for column in range(5):
            self.columnconfigure(column, weight=1)
        for row in range(6):
            self.rowconfigure(row, weight=1)

        self.bind("<KeyPress>", self.keypress)

        self.input = ''
        self.operation = ''
        self.clearinput = False

    def keypress(self,e):
        symbol = e.keysym
        #print(symbol)

        if (symbol == 'BackSpace'):
            self.backspace()

        if (symbol == 'equal' or symbol == 'KP_Enter' or symbol == 'Return'):
            self.equalpressed()

        if (symbol.lower() == 'c'):
            self.clear('C')

        if (e.char in "+-/*^"):
            self.operationpressed(e.char)

        if (e.char.isdigit() or e.char == '.'):
            self.numberpressed(e.char)

    def backspace(self):
        if (len(self.Display["text"]) > 0 and self.Display["text"] != '0'):
            self.Display.configure(text=self.Display["text"][:-1])

        self.Display["text"] = self.Display["text"] if self.Display["text"] else '0'

    def clear(self, command):
        self.Display.configure(text="0")
        if (command == "C"):
            self.input = ''
            self.operation = ''

    def equalpressed(self):
        result = 0.0

        if(not self.operation or not self.input):
            return

        input1 = float(self.input)
        input2 = float(self.Display["text"])

        self.input = ''

        if (self.operation == '+'):
            result = input1 + input2
        if (self.operation == '-'):
            result = input1 - input2
        if (self.operation == '*'):
            result = input1 * input2
        if (self.operation == '/'):
            if (input2 == 0.0):
                self.Display.configure(text="error")
                self.clearinput = True
                return
            result = input1 / input2
        if (self.operation == '^'):
            result = input1 ** input2

        self.Display.configure(text=self.cleardotzero(str(result)))
        self.clearinput = True

    def cleardotzero(self,fpnumber):
        return (fpnumber.replace('.0', '') if fpnumber.endswith('.0') else fpnumber)

    def sqrootpressed(self):
        self.Display.configure(text=str(math.sqrt(float(self.Display["text"]))))
        self.clearinput = True

        self.Display.configure(text=self.cleardotzero(self.Display["text"]))

    def operationpressed(self, operation):
        self.equalpressed()
        self.input = self.Display["text"][:]
        self.operation = operation
        self.clearinput = True

    def numberpressed(self, numberpressed):
        if (numberpressed == '.' and '.' in self.Display["text"]):
            return

        if (numberpressed == "+-"):
            self.Display["text"] = self.Display["text"].lstrip("-") \
                if self.Display["text"].startswith('-') else "-" + self.Display["text"]
            return

        if(self.clearinput):
            self.Display.configure(text="")
            self.clearinput = False

        self.Display.configure(text=self.Display["text"].lstrip('0') + numberpressed)

def run():
    calc = Calc()
    calc.mainloop()