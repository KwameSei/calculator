from re import S
import tkinter as tk
import parser
from math import factorial

root = tk.Tk()
root.geometry("500x650")
root.configure(bg='black')
root.title("Calculator")

# i keeps the track of current position on the input text field
i = 0
# Receives the digit as parameter and display it on the input field
def get_num(num):
    global i
    display.insert(i,num)
    i+=1

#The display panel
display = tk.Entry(root)
display.grid(row=0, columnspan=6, sticky="nsew")

clear_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='C')
clear_button.grid(row=2, column=1, padx=10, pady=10)
another_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='CE')
another_button.grid(row=2, column=2, padx=10, pady=10)
opening_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='(')
opening_button.grid(row=2, column=3, padx=10, pady=10)
close_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text=')')
close_button.grid(row=2, column=4, padx=10, pady=10)
del_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='red', fg='white', text='Del')
del_button.grid(row=2, column=5, padx=10, pady=10)
decimal_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='.')
decimal_button.grid(row=6, column=4, padx=10, pady=10)
equal_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='green', fg='white', text='=')
equal_button.grid(row=6, column=5, padx=10, pady=10)
equal_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='^2')
equal_button.grid(row=3, column=5, padx=10, pady=10)
equal_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='exp')
equal_button.grid(row=4, column=5, padx=10, pady=10)
equal_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, bg='blue', fg='white', text='pi')
equal_button.grid(row=5, column=5, padx=10, pady=10)


#Creating Arithmetic operation buttons
add_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_operation("+"), width=3, height=1, bg='blue', fg='white', text='+')
add_button.grid(row=3, column=1, padx=10, pady=10)
sub_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_operation("-"), width=3, height=1, bg='blue', fg='white', text='-')
sub_button.grid(row=4, column=1, padx=10, pady=10)
mul_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_operation("*"), width=3, height=1, bg='blue', fg='white', text='x')
mul_button.grid(row=5, column=1, padx=10, pady=10)
div_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_operation("/"), width=3, height=1, bg='blue', fg='white', text='/')
div_button.grid(row=6, column=1, padx=10, pady=10)
mod_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_operation("%"), width=3, height=1, bg='blue', fg='white', text='%')
mod_button.grid(row=6, column=2, padx=10, pady=10)


one_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(1), width=3, height=1, text='1')
one_button.grid(row=3, column=2, padx=10, pady=10)
two_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(2), width=3, height=1, text='2')
two_button.grid(row=3, column=3, padx=10, pady=10)
three_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(3), width=3, height=1, text='3')
three_button.grid(row=3, column=4, padx=10, pady=10)
four_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(4), width=3, height=1, text='4')
four_button.grid(row=4, column=2, padx=10, pady=10)
five_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(5), width=3, height=1, text='5')
five_button.grid(row=4, column=3, padx=10, pady=10)
six_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(6), width=3, height=1, text='6')
six_button.grid(row=4, column=4, padx=10, pady=10)
seven_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(7), width=3, height=1, text='7')
seven_button.grid(row=5, column=2, padx=10, pady=10)
eight_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(8), width=3, height=1, text='8')
eight_button.grid(row=5, column=3, padx=10, pady=10)
nine_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(9), width=3, height=1, text='9')
nine_button.grid(row=5, column=4, padx=10, pady=10)
zero_button = tk.Button(root, font=('Helvetica', 20), command=lambda :get_num(0), width=3, height=1, text='0')
zero_button.grid(row=6, column=3, padx=10, pady=10)

root.mainloop()