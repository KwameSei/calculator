import tkinter as tk
from turtle import color

root = tk.Tk()
root.geometry("500x650")
root.configure(bg='black')
root.title("Calculator")

#The display panel
display = tk.Entry(root, font=("Helvetica bold", 15), text="0")
display.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

one_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='1')
one_button.grid(row=3, column=1, padx=10, pady=10)
two_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='2')
two_button.grid(row=3, column=2, padx=10, pady=10)
three_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='3')
three_button.grid(row=3, column=3, padx=10, pady=10)
four_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='4')
four_button.grid(row=4, column=1, padx=10, pady=10)
five_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='5')
five_button.grid(row=4, column=2, padx=10, pady=10)
six_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='6')
six_button.grid(row=4, column=3, padx=10, pady=10)
seven_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='7')
seven_button.grid(row=5, column=1, padx=10, pady=10)
eight_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='8')
eight_button.grid(row=5, column=2, padx=10, pady=10)
nine_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='9')
nine_button.grid(row=5, column=3, padx=10, pady=10)
zero_button = tk.Button(root, font=('Helvetica', 20), width=3, height=1, text='0')
zero_button.grid(row=6, column=2, padx=10, pady=10)

root.mainloop()