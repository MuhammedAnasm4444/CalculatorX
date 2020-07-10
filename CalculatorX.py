from tkinter import *
from tkinter import font as tkFont
import math
from functools import reduce  
import operator

sum_operator = False
minus_operator = False
is_clicked = False
multiply_operator = False
division_operator = False
square_operator = False
percentage_operator = False
power_operator = False
sin_operator = False
cos_operator = False
tan_operator = False
factorial_operator = False
sin_inverse_operator = False
cos_inverse_operator = False
tan_inverse_operator = False
value = []
arbitary_sum_operator = False
arbitary_minus_operator = False
equal_clicked = False


#window for Calculator
window = Tk()
window.geometry("210x369")
window.resizable(False,False)
window.title("CalculatorX")
window.configure(bg="dark slate gray")

# Creating  Calculating area
label_value = StringVar()
label_value.set("")


#Button Click commands
# defining button  "7" function
def button7_click():
        global is_clicked
        if is_clicked  :
                
                label_value.set("7")
                is_clicked = False
                print("worked")
        else:
                 label_value.set(label_value.get() + "7")
# defining button "8" function 
def button8_click():
        global is_clicked

        if is_clicked == True:

                label_value.set("8")
                is_clicked = False
        else:
                 label_value.set(label_value.get() + "8")
# defining button  "9" function
def button9_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("9")
                is_clicked = False
        else:
                 label_value.set(label_value.get() + "9")
# defining button  "4" function
def button4_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("4")
                is_clicked = False
        else:
                 label_value.set(label_value.get() + "4")
# defining button  "5" function
def button5_click():
        global is_clicked
        if is_clicked == True:

                label_value.set("5")
                is_clicked = False
        else:

                label_value.set(label_value.get() + "5")
# defining button  "6" function
def button6_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("6")
                is_clicked = False
        else:

                 label_value.set(label_value.get() + "6")
# defining button  "1" function
def button1_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("1")
                is_clicked = False

        else:
                label_value.set(label_value.get() + "1")
# defining button  "2" function
def button2_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("2")
                is_clicked = False
        else:

                 label_value.set(label_value.get() + "2")
# defining button  "3" function
def button3_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("3")
                is_clicked = False
        else:
                 label_value.set(label_value.get() + "3")
# defining button  "0" function
def button0_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("0")
                is_clicked = False
        else:

                label_value.set(label_value.get() + "0")
# defining button  "." function
def button_dot_click():
        global is_clicked
        if is_clicked == True:
                label_value.set("0")
                is_clicked = False
        else:
                label_value.set(label_value.get() + ".")
# defining button  "C" function
def clear_clicked():
        label_value.set("")
        global old_value
        global minus_operator 
        minus_operator = False
        global sum_operator
        sum_operator = False
        global multiply_operator
        multiply_operator = False
        global division_operator
        division_operator = False
        global square_operator
        square_operator = False
        global percentage_operator
        percentage_operator = False
        global power_operator
        power_operator = False

        global sin_operator
        sin_operator = False
        global cos_operator
        cos_operator = False
        global tan_operator
        tan_operator = False
        
        global factorial_operator
        factorial_operator = False
        global sin_inverse_operator
        sin_inverse_operator =  False
        global cos_inverse_operator
        cos_inverse_operator = False
        global tan_inverse_operator
        tan_inverse_operator = False

        global new_value
        old_value = "0"
        new_value = "0"
        global value
        value = []

# Math Operations



# when '+'button  




def sum_operation():

        global is_clicked
        is_clicked = True
        

        global value
        value.append(label_value.get())
    
        value.append('+')


# when '-' button clicked
def minus_operation():
        global value
        global is_clicked
        is_clicked = True
        global value
        value.append(label_value.get())
        value.append('-')

        
# when '*'  button clicked
def product_operation():
        global value
        global is_clicked
        is_clicked = True
        value.append(label_value.get())
        value.append('*')
        


# when '/' button clicked
def division_operation():
        global value
        global is_clicked
        is_clicked = True
        value.append(label_value.get())
        value.append('/')



# when '%' button clicked
def percentage_operation():
        global is_clicked
        is_clicked = True
        global percentage_operator
        percentage_operator = True
        global old_value
        old_value = label_value.get()


# when '√' button clicked
def square_operation():
        label_value.set("√(")
        global square_operator
        square_operator = True


# when 'x^y' button clicked
def power_operation():
        global is_clicked
        is_clicked = True
        global power_operator
        power_operator = True
        global old_value
        old_value = label_value.get()



# when 'sin' button clicked
def sin_operation():
        label_value.set("sin")
        global sin_operator
        sin_operator = True


# when 'cos' button clicked
def cos_operation():
        label_value.set("cos")
        global cos_operator
        cos_operator = True


# when 'tan' button clicked
def tan_operation():
        label_value.set("tan")
        global tan_operator
        tan_operator = True


# when "!" button clicked
def factorial_operation():
        global factorial_operator
        global old_value
        old_value = label_value.get()
        factorial_operator =True
        old_value = label_value.set(old_value +"!")

#when "sin-1" button clicked
def sin_inverse_operation():
        label_value.set("sin-1")
        global sin_inverse_operator
        sin_inverse_operator = True

#when "cos-1" button clicked
def cos_inverse_operation():
        label_value.set("cos-1")
        global cos_inverse_operator
        cos_inverse_operator = True

# when "tan-1" button clicked
def tan_inverse_operation():
        label_value.set("tan-1")
        global tan_inverse_operator
        tan_inverse_operator = True

# when "del" button clicked
def button_backspace():
        global old_value
        old_value = label_value.get()
        old_value = old_value[:-1]
        if old_value == "":
                old_value = "0"
        label_value.set(old_value)


#Defining all Operation
def equal_click():
# global variables
        global sum_operator
        global new_value
        global old_value
        global value
        global result
        global minus_operator
        global multiply_operator
        global division_operator
        global square_operators
        global percentage_operator
        global power_operator

        global sin_operator
        global cos_operator
        global tan_operator
        global square_operator
        global factorial_operator
        global sin_inverse_operator
        global cos_inverse_operator
        global tan_inverse_operator
        global equal_clicked
        value.append(label_value.get())

        equal_clicked = True
        print(value)
        result = value[0]
        label_value.set(result)
        print(result)
    

        print(value)
    # operating addition, subtraction, multiplication and division
    # for muliple operation
    # 


        for i in range(len(value)):
                try:


                    
            


                  if value[1] == '+':


                      xsum = float(value[0]) + float(value[2])
                      xsum = str(xsum)

                      print(xsum)
                      value.pop(0)

                      value.pop(0)

                      value.pop(0) 
                      print(value)
                      value.insert(0,xsum)
                      print(value)

                  elif value[1] == '-':
                      xdifference = float(value[0]) - float(value[2])
                      xdifference = str(xdifference)
                      value.pop(0)
                    
                      value.pop(0)
                    
                      value.pop(0)
                      print(value) 
                      value.insert(0,xdifference)
                      print(value)
                  elif value[1] == '*':
                      xmultiply = float(value[0]) * float(value[2])
                      xmultiply = str(xmultiply)
                      value.pop(0)
                      value.pop(0)
                      value.pop(0)
                      print(value)
                      value.insert(0,xmultiply)
                  elif value[1] == '/':
                      xdivision = float(value[0]) / float(value[2])
                      xdivision = str(xdivision)
                      value.pop(0)
                      value.pop(0)
                      value.pop(0)
                      print(value)
                      value.insert(0,xdivision)
                      print(value)
                except Exception:
            
                    break



        equal_clicked = True
        print(value)
        result = value[0]
        label_value.set(result)
        print(result)


        # Operating square root
        if square_operator == True:
                new_value = label_value.get()
                new_value = new_value.replace('√(', '')
                print(new_value)
                result = math.sqrt(float(new_value))
                label_value.set(str(result))
                square_operator = False


        # Operating percentage 
        elif percentage_operator == True:
                new_value = label_value.get()
                result = 100 * float(old_value)/float(new_value)
                label_value.set(str(result))
                percentage_operator = False
        
        # Operating power (exponential)
        elif power_operator == True:
                
                new_value = label_value.get()
                
                result = float(old_value) ** float(new_value)
                label_value.set(str(result))
                power_operator = False

        # Trignometric Functions

        # Operating sin
        elif sin_operator == True:
                new_value = label_value.get()
                new_value = new_value.replace('sin', '')
                print(new_value)
                result = math.sin(float(new_value))
                label_value.set(str(result))
                sin_operator = False

        # Operating cos
        elif cos_operator == True:
                new_value = label_value.get()
                new_value = new_value.replace('cos', '')
                print(new_value)
                result = math.cos(float(new_value))
                label_value.set(str(result))
                cos_operator = False

        # Operating tan
        elif tan_operator == True:
                new_value = label_value.get()
                new_value = new_value.replace('tan', '')
                print(new_value)
                result = math.tan(float(new_value))
                label_value.set(str(result))
                tan_operator = False
        # Operating factorial
        elif factorial_operator == True:
                old_value = label_value.get()

                result = old_value.replace("!"," ")
                
                try:    
                        
                     result = math.factorial(float(result))
                     label_value.set(str(result))
                except Exception:
                        label_value.set("something wrong")

                factorial_operator = False
        elif sin_inverse_operator == True:

                new_value = label_value.get()
                new_value = new_value.replace('sin-1', '')
                result = math.asin(float(new_value))
                label_value.set(str(result))
                sin_inverse_operator = False

        elif cos_inverse_operator == True:

                new_value = label_value.get()
                new_value = new_value.replace('cos-1', '')
                result = math.acos(float(new_value))
                label_value.set(str(result))
                sin_inverse_operator = False
        elif tan_inverse_operator == True:

                new_value = label_value.get()
                new_value = new_value.replace('tan-1', '')
                result = math.atan(float(new_value))
                label_value.set(str(result))
                sin_inverse_operator = False






        else:
                print('ok')

                
#Creating Workspace
calculation = Entry(window, textvariable = label_value, font=("Verdana", 15, ), bd = 12,
                                        insertwidth=4, width=14, justify=RIGHT,state = DISABLED)
calculation.grid(columnspan=4)



#Creating Buttons
button7 = Button(window, text='7', bg="gainsboro",command = button7_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button7.grid(row=2, column=0, sticky=W)
button8 = Button(window, text='8', bg="gainsboro",command = button8_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button8.grid(row=2, column=1, sticky=W)

button9 = Button(window, text='9',bg="gainsboro",command = button9_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button9.grid(row=2, column=2, sticky=W)




button4 = Button(window, text='4', bg="gainsboro",command = button4_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button4.grid(row=3, column=0, sticky=W)
button5 = Button(window, text='5',  bg="gainsboro",command = button5_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button5.grid(row=3, column=1, sticky=W)
button6 = Button(window, text='6',  bg="gainsboro",command = button6_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button6.grid(row=3, column=2, sticky=W)



button1 = Button(window, text='1', bg="gainsboro",command = button1_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button1.grid(row=4, column=0, sticky=W)
button2 = Button(window, text='2', bg="gainsboro",command = button2_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button2.grid(row=4, column=1, sticky=W)
button3 = Button(window, text='3',  bg="gainsboro",command = button3_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button3.grid(row=4, column=2, sticky=W)


button0 = Button(window, text='0', bg="gainsboro",command = button0_click,
                                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button0.grid(row=5, column=0, sticky=W)
button_dot = Button(window, text='.',  bg="gainsboro",command = button_dot_click,
                                            bd=3, padx=15, pady=5, font=("Helvetica", 14, "bold"))
button_dot.grid(row=5, column=1)



#   Math signs

# Making plus button
button_plus = Button(window, text='+', bg="gray70",command = sum_operation,
                                         bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=2, column=3, sticky=W)

# Making minus button
button_minus = Button(window, text='-',  bg="gray70",command = minus_operation,
                                            bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, sticky=W)

# Making multiplication button
button_multiply = Button(window, text='*', bg="gray70",command = product_operation,
                                                 bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=4, column=3, )

# Making division button
button_division = Button(window, text='/', bg="gray70",command = division_operation,
                                                 bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=5, column=3, )

# Making equal button
button_equal = Button(window, text='=',  bg='orange',command = equal_click,
                                            bd=3, padx=12, pady=5, font=("Arial", 14))
button_equal.grid(row=5, column=2, )

# Making percentage
button_percent = Button(window, text='%', bg="gray70",command = percentage_operation,
                                                 bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
button_percent.grid(row=1, column=3, )

# Making clear button
button_clear = Button(window, text='C', bg='gray70',command = clear_clicked,
                                            bd=3, padx=11, pady=5, font=("Helvetica", 14))
button_clear.grid(row=1, column=0)

# Making square button
button_sqrt = Button(window, text='√',  bg="gray70",command = square_operation,
                                                bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button_sqrt.grid(row=1, column=1, sticky=W)


# Making power(exponential) button
button_power = Button(window, text='x^y', bg="gray70",command = power_operation,
                                    bd=3, padx=6, pady=5, font=("Helvetica", 14))
button_power.grid(row=1, column=2, sticky=W)



button_sin = Button(window, text='sin', bg="gray70",command = sin_operation,
                                                 bd=4, padx=12, pady=5, font=("Helvetica", 8, ""))
button_sin.grid(row=6, column=0, )
button_cos = Button(window, text='cos', bg="gray70",command = cos_operation,
                                                 bd=4, padx=12, pady=5, font=("Helvetica", 8, ""))
button_cos.grid(row=6, column=1, )

button_tan = Button(window, text='tan', bg="gray70",command = tan_operation,
                                                 bd=4, padx=12, pady=5, font=("Helvetica", 8, ""))
button_tan.grid(row=6, column=2, )

button_factorial = Button(window, text='!', bg="gray70",command = factorial_operation,
                                                 bd=4, padx=18, pady=5, font=("Helvetica", 8, "bold"))
button_factorial.grid(row=6, column=3, )


button_sin_inverse = Button(window, text='sin-1', bg="gray70",command = sin_inverse_operation,
                                                 bd=4, padx=12, pady=8, font=("Helvetica", 6, ""))
button_sin_inverse.grid(row=7, column=0, )

button_cos_inverse = Button(window, text='cos-1', bg="gray70",command = cos_inverse_operation,
                                                 bd=4, padx=12, pady=8, font=("Helvetica", 6, ""))
button_cos_inverse.grid(row=7, column=1, )

button_tan_inverse = Button(window, text='tan-1', bg="gray70",command = tan_inverse_operation,
                                                 bd=4, padx=12, pady=8, font=("Helvetica", 6, ""))
button_tan_inverse.grid(row=7, column=2, )


button_backspace = Button(window, text='del', bg="light slate gray",command = button_backspace,
                                                 bd=7, padx=11, pady=5, font=("Helvetica", 7, ""))
button_backspace.grid(row=7, column=3, )
window.mainloop()