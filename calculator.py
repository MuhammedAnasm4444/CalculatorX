from tkinter import *
from tkinter import font as tkFont
window = Tk()
window.geometry("210x295")

window.title("Calculator")
window.configure(bg="dark slate gray")
label_value = StringVar()

helv36 = tkFont.Font(weight = "normal")
calculation = Entry(window, textvariable = "label_value", font=("Verdana", 15, ), bd = 12,
                    insertwidth=4, width=14, justify=RIGHT)
calculation.grid(columnspan=4)
button7 = Button(window, text='7', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button7.grid(row=2, column=0, sticky=W)
button8 = Button(window, text='8', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button8.grid(row=2, column=1, sticky=W)
button9 = Button(window, text='9',bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button9.grid(row=2, column=2, sticky=W)
button4 = Button(window, text='4', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button4.grid(row=3, column=0, sticky=W)
button5 = Button(window, text='5',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button5.grid(row=3, column=1, sticky=W)
button6 = Button(window, text='6',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button6.grid(row=3, column=2, sticky=W)
button1 = Button(window, text='1', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button1.grid(row=4, column=0, sticky=W)
button2 = Button(window, text='2', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button2.grid(row=4, column=1, sticky=W)
button3 = Button(window, text='3',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button3.grid(row=4, column=2, sticky=W)
button0 = Button(window, text='0', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button0.grid(row=5, column=0, sticky=W)
button_float = Button(window, text='.',  bg="gainsboro",
                      bd=3, padx=15, pady=5, font=("Helvetica", 14, "bold"))
button_float.grid(row=5, column=1)

#   Math signs
button_plus = Button(window, text='+', bg="gray70",
                     bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=2, column=3, sticky=W)
button_minus = Button(window, text='-',  bg="gray70",
                      bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, sticky=W)
button_multiply = Button(window, text='*', bg="gray70",
                         bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=4, column=3, )
button_division = Button(window, text='/', bg="gray70",
                         bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=5, column=3, )
button_equal = Button(window, text='=',  bg='orange',
                      bd=3, padx=12, pady=5, font=("Arial", 14))
button_equal.grid(row=5, column=2, )

button_percent = Button(window, text='%', command=lambda: percent(),  bg="gray70",
                         bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
button_percent.grid(row=1, column=3, )

button_clear = Button(window, text='C', bg='gray70',
                      bd=3, padx=11, pady=5, font=("Helvetica", 14))
button_clear.grid(row=1, column=0)
button_sqrt = Button(window, text='√',  bg="gray70",
                        bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button_sqrt.grid(row=1, column=1, sticky=W)
button_x = Button(window, text='x^y', bg="gray70",
                  bd=3, padx=6, pady=5, font=("Helvetica", 14))
button_x.grid(row=1, column=2, sticky=W)






window.mainloop()