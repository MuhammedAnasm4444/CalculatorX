from tkinter import *
from tkinter import font as tkFont
import math


sum_operator = False
minus_operator = False
is_clicked = False
multiply_operator = False
division_operator = False
square_operator = False
percentage_operator = False


#window for Calculator
window = Tk()
window.geometry("210x295")
window.title("Calculator")
window.configure(bg="dark slate gray")


label_value = StringVar()
label_value.set("")
num_list= [0,1,2,3,4,5,6,7,8,9]
#Button Click commands
def button7_click():
	global is_clicked
	if is_clicked  :
		
		label_value.set("7")
		is_clicked = False
		print("worked")
	else:
		 label_value.set(label_value.get() + "7")

def button8_click():
	global is_clicked

	if is_clicked == True:

		label_value.set("8")
		is_clicked = False
	else:
		 label_value.set(label_value.get() + "8")

def button9_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("9")
		is_clicked = False
	else:
		 label_value.set(label_value.get() + "9")

def button4_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("4")
		is_clicked = False
	else:
		 label_value.set(label_value.get() + "4")

def button5_click():
	global is_clicked
	if is_clicked == True:

		label_value.set("5")
		is_clicked = False
	else:

		label_value.set(label_value.get() + "5")

def button6_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("6")
		is_clicked = False
	else:

		 label_value.set(label_value.get() + "6")

def button1_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("1")
		is_clicked = False

	else:
		label_value.set(label_value.get() + "1")

def button2_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("2")
		is_clicked = False
	else:

		 label_value.set(label_value.get() + "2")

def button3_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("3")
		is_clicked = False
	else:
		 label_value.set(label_value.get() + "3")

def button0_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("0")
		is_clicked = False
	else:

		label_value.set(label_value.get() + "0")

def button_dot_click():
	global is_clicked
	if is_clicked == True:
		label_value.set("0")
		is_clicked = False
	else:
		label_value.set(label_value.get() + ".")

def clear_clicked():
	label_value.set(" ")
	global old_value
	global new_value
	old_value = 0
	new_value = 0

# Math Operations
# when '+'button  clicked
def sum_operation():
	global is_clicked
	is_clicked = True
	global sum_operator
	sum_operator =True
	global old_value
	old_value  = label_value.get()

	
# when '-' button clicked
def minus_operation():
	global is_clicked
	is_clicked = True
	global minus_operator
	minus_operator = True
	global old_value
	old_value = label_value.get()
	
# when '*'	button clicked
def product_operation():
	global is_clicked
	is_clicked = True
	global multiply_operator
	multiply_operator = True
	global old_value
	old_value = label_value.get()

# when '/' button clicked
def division_operation():
	global is_clicked
	is_clicked = True
	global division_operator
	division_operator = True
	global old_value
	old_value = label_value.get()

def percentag_operation():
	global is_clicked
	is_clicked = True
	global percentage_operator
	percentage_operator = True
	global old_value
	old_value = label_value.get()

def square_operation():
	label_value.set("√(")
	global square_operator
	square_operator = True



#Defining all Operation
def equal_click():
	global sum_operator
	global new_value
	global result
	global minus_operator
	global multiply_operator
	global division_operator
	global square_operator
	# Operating sum
	if sum_operator == True:
		new_value = label_value.get()
		result = float(new_value) + float(old_value)
		label_value.set(str(result))
		sum_operator = False
		print('added')
	# Operating difference
	elif minus_operator ==True:
		new_value = label_value.get()
		result =  float(old_value) - float(new_value)
		label_value.set(str(result))
		minus_operator = False
		print('subracted')
	# Operating product
	elif multiply_operator == True:
		new_value = label_value.get()
		result = float(old_value)*float(new_value)
		label_value.set(str(result))
		multiply_operator = False
	# Operating division
	elif division_operator == True:
		new_value = label_value.get()
		result = float(old_value)/float(new_value)
		label_value.set(str(result))
		division_operator = False
		
	elif square_operator == True:
		new_value = label_value.get()
		new_value = new_value.replace('√(', '')
		print(new_value)
		result = math.sqrt(float(new_value))
		label_value.set(str(result))
		square_operator = False
	elif percentage_operator == True:
		new_value = label_value.get()
		result = 100 * float(old_value)/float(new_value)
		label_value.set(str(result))
		percentage_operator = False
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
button_plus = Button(window, text='+', bg="gray70",command = sum_operation,
					 bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=2, column=3, sticky=W)
button_minus = Button(window, text='-',  bg="gray70",command = minus_operation,
					  bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, sticky=W)
button_multiply = Button(window, text='*', bg="gray70",command = product_operation,
						 bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=4, column=3, )
button_division = Button(window, text='/', bg="gray70",
						 bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=5, column=3, )
button_equal = Button(window, text='=',  bg='orange',command = equal_click,
					  bd=3, padx=12, pady=5, font=("Arial", 14))
button_equal.grid(row=5, column=2, )

button_percent = Button(window, text='%', bg="gray70",command = percentage_operation,
						 bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
button_percent.grid(row=1, column=3, )

button_clear = Button(window, text='C', bg='gray70',command = clear_clicked,
					  bd=3, padx=11, pady=5, font=("Helvetica", 14))
button_clear.grid(row=1, column=0)
button_sqrt = Button(window, text='√',  bg="gray70",command = square_operation,
						bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button_sqrt.grid(row=1, column=1, sticky=W)
button_x = Button(window, text='x^y', bg="gray70",
				  bd=3, padx=6, pady=5, font=("Helvetica", 14))
button_x.grid(row=1, column=2, sticky=W)






window.mainloop()