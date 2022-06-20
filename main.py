import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Title
        self.title("Ha Noi University of Science and Technology")
        self.iconbitmap("./assets/title.ico")

        # Window
        w_x = 400
        w_y = 200
        self.geometry(f"{w_x}x{w_y}")
        self.resizable(0, 0)

        # Frame
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=4)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Number
        wd = 10
        # 7
        button_7 = ttk.Button(self, text=7, width=wd, command=self.button7)
        button_7.grid(column=0, row=2, sticky=tk.N, padx=10, pady=5)
        # 8
        button_8 = ttk.Button(self, text=8, width=wd, command=self.button8)
        button_8.grid(column=1, row=2, sticky=tk.N, padx=5, pady=5)
        # 9
        button_9 = ttk.Button(self, text=9, width=wd, command=self.button9)
        button_9.grid(column=2, row=2, sticky=tk.N, padx=5, pady=5)
        # 4
        button_4 = ttk.Button(self, text=4, width=wd, command=self.button4)
        button_4.grid(column=0, row=3, sticky=tk.N, padx=5, pady=5)
        # 5
        button_5 = ttk.Button(self, text=5, width=wd, command=self.button5)
        button_5.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)
        # 6
        button_6 = ttk.Button(self, text=6, width=wd, command=self.button6)
        button_6.grid(column=2, row=3, sticky=tk.N, padx=5, pady=5)
        # 1
        button_1 = ttk.Button(self, text=1, width=wd, command=self.button1)
        button_1.grid(column=0, row=4, sticky=tk.N, padx=5, pady=5)\
        # 2
        button_2 = ttk.Button(self, text=2, width=wd, command=self.button2)
        button_2.grid(column=1, row=4, sticky=tk.N, padx=5, pady=5)
        # 3
        button_3 = ttk.Button(self, text=3, width=wd, command=self.button3)
        button_3.grid(column=2, row=4, sticky=tk.N, padx=5, pady=5)
        # 0
        button_0 = ttk.Button(self, text=0, width=wd, command=self.button0)
        button_0.grid(column=0, row=5, sticky=tk.N, padx=5, pady=5)
        # .
        button_f = ttk.Button(self, text='.', width=wd, command=self.buttonDot)
        button_f.grid(column=1, row=5, sticky=tk.N, padx=5, pady=5)
        # 3
        button_e = ttk.Button(self, text='=', width=wd, command=self.result)
        button_e.grid(column=2, row=5, sticky=tk.N, padx=5, pady=5)
        
        # Operator
        # +
        button_p = ttk.Button(self, text='+', width=wd, command=self.buttonP)
        button_p.grid(column=3, row=2, sticky=tk.N, padx=5, pady=5)
        # -
        button_s = ttk.Button(self, text='-', width=wd, command=self.buttonS)
        button_s.grid(column=3, row=3, sticky=tk.N, padx=5, pady=5)
        # *
        button_m = ttk.Button(self, text='*', width=wd, command=self.buttonM)
        button_m.grid(column=3, row=3, sticky=tk.N, padx=5, pady=5)
        # /
        button_d = ttk.Button(self, text='/', width=wd, command=self.buttonD)
        button_d.grid(column=3, row=4, sticky=tk.N, padx=5, pady=5)

        # AC
        button_ac = ttk.Button(self, text="AC", width=wd, command=self.buttonAC)
        button_ac.grid(column=3, row=5, sticky=tk.N, padx=5, pady=5)

        # Text
        self.text = tk.Text(self)
        self.text.grid(columnspan=6, row=0, padx=5, pady=5)
        self.re = ""
    
    def insertText(self):
        # Text
        self.text.insert("end", self.re)

    def result(self):
        self.text.insert("end", self.cal())

    def buttonAC(self):
        self.re = ""
        self.text.delete("1.0", "end")

    def cal(self):
        try:
            # +
            x = self.re.find("+")
            if x != -1:
                l = self.re.split("+")
                return  '=' + str(float(l[0]) + float(l[1]))

            # -
            x = self.re.find("-")
            if x != -1:
                l = self.re.split("-")
                return '=' +  str(float(l[0]) - float(l[1]))

            # *
            x = self.re.find("*")
            if x != -1:
                l = self.re.split("*")
                return '=' +  str(float(l[0]) * float(l[1]))
            
            # /
            x = self.re.find("/")
            if x != -1:
                l = self.re.split("/")
                return '=' + str(float(l[0]) / float(l[1]))
        except:
            return "\tError"
    
    # +
    def buttonP(self):
        self.re = self.re + '+'
        self.text.insert("end", '+')

    # -
    def buttonS(self):
        self.re = self.re + '-'
        self.text.insert("end", '-')

    # *
    def buttonM(self):
        self.re = self.re + '*'
        self.text.insert("end", '*')

    # /
    def buttonD(self):
        self.re = self.re + '/'
        self.text.insert("end", '/')

    def buttonDot(self):
        self.re = self.re + '.'
        self.text.insert("end", '.')
    def button0(self):
        self.re = self.re + '0'
        self.text.insert("end", '0')

    def button1(self):
        self.re = self.re + '1'
        self.text.insert("end", '1')

    def button2(self):
        self.re = self.re + '2'
        self.text.insert("end", '2')

    def button3(self):
        self.re = self.re + '3'
        self.text.insert("end", '3')

    def button4(self):
        self.re = self.re + '4'
        self.text.insert("end", '4')

    def button5(self):
        self.re = self.re + '5'
        self.text.insert("end", '5')

    def button6(self):
        self.re = self.re + '6'
        self.text.insert("end", '6')

    def button7(self):
        self.re = self.re + '7'
        self.text.insert("end", '7')
    
    def button8(self):
        self.re = self.re + '8'
        self.text.insert("end", '8')
    
    def button9(self):
        self.re = self.re + '9'
        self.text.insert("end", '9')

        
        
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
