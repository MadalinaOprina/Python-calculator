import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN, NORMAL
import math

window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

def myclick(number):
    entry.insert(tk.END, number)

def add_parenthesis(parenthesis):
    entry.insert(tk.END, parenthesis)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

def backspace():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text)-1, tk.END)

def percentage():
    try:
        current_value = float(entry.get())
        result = current_value / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

def special_function(func):
    try:
        current_text = entry.get()
        result = ''
        if func == 'sin':
            result = str(math.sin(math.radians(float(current_text))))
        elif func == 'cos':
            result = str(math.cos(math.radians(float(current_text))))
        elif func == 'tan':
            result = str(math.tan(math.radians(float(current_text))))
        elif func == 'cot':
            result = str(1 / math.tan(math.radians(float(current_text))))
        elif func == 'log':
            result = str(math.log10(float(current_text)))
        elif func == 'ln':
            result = str(math.log(float(current_text)))
        elif func == 'exp':
            result = str(math.exp(float(current_text)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

def toggle_trig_buttons():
    if button_sin.winfo_ismapped():
        button_sin.grid_remove()
        button_cos.grid_remove()
        button_tan.grid_remove()
        button_cot.grid_remove()
        button_ln.grid_remove()
        button_log.grid_remove()
        button_exp.grid_remove()
        button_pi.grid_remove()
        button_e.grid_remove()
        button_trig.config(text='Trig')
    else:
        button_sin.grid()
        button_cos.grid()
        button_tan.grid()
        button_cot.grid()
        button_ln.grid()
        button_log.grid()
        button_exp.grid()
        button_pi.grid()
        button_e.grid()
        button_trig.config(text='Scientific')

button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_open_parenthesis = tk.Button(master=frame, text='(', padx=15, pady=5, width=3, command=lambda: add_parenthesis('('))
button_open_parenthesis.grid(row=4, column=0, pady=2)
button_close_parenthesis = tk.Button(master=frame, text=')', padx=15, pady=5, width=3, command=lambda: add_parenthesis(')'))
button_close_parenthesis.grid(row=4, column=2, pady=2)
button_add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)
button_backspace = tk.Button(master=frame, text='←', padx=15, pady=5, width=3, command=backspace)
button_backspace.grid(row=5, column=2, pady=2)
button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=6, column=0, pady=2)
button_div = tk.Button(master=frame, text="/", padx=15, pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=1, pady=2)
button_clear = tk.Button(master=frame, text="CLEAR", padx=15, pady=5, width=3, command=clear)
button_clear.grid(row=6, column=2, pady=2)
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)
button_percentage = tk.Button(master=frame, text='%', padx=15, pady=5, width=3, command=percentage)
button_percentage.grid(row=7, column=0, pady=2)

button_trig = tk.Button(master=frame, text='Trig', padx=15, pady=5, width=3, command=toggle_trig_buttons)
button_trig.grid(row=7, column=2, pady=2)


# Trigonometry and other special function buttons, initially hidden
button_sin = tk.Button(master=frame, text='sin', padx=15, pady=5, width=3, command=lambda: special_function('sin'))
button_sin.grid(row=8, column=0, pady=2)
button_sin.grid_remove()

button_cos = tk.Button(master=frame, text='cos', padx=15, pady=5, width=3, command=lambda: special_function('cos'))
button_cos.grid(row=8, column=1, pady=2)
button_cos.grid_remove()

button_tan = tk.Button(master=frame, text='tan', padx=15, pady=5, width=3, command=lambda: special_function('tan'))
button_tan.grid(row=8, column=2, pady=2)
button_tan.grid_remove()

button_cot = tk.Button(master=frame, text='cot', padx=15, pady=5, width=3, command=lambda: special_function('cot'))
button_cot.grid(row=9, column=0, pady=2)
button_cot.grid_remove()

button_ln = tk.Button(master=frame, text='ln', padx=15, pady=5, width=3, command=lambda: special_function('ln'))
button_ln.grid(row=9, column=1, pady=2)
button_ln.grid_remove()

button_log = tk.Button(master=frame, text='log', padx=15, pady=5, width=3, command=lambda: special_function('log'))
button_log.grid(row=9, column=2, pady=2)
button_log.grid_remove()

button_exp = tk.Button(master=frame, text='exp', padx=15, pady=5, width=3, command=lambda: special_function('exp'))
button_exp.grid(row=10, column=0, pady=2)
button_exp.grid_remove()

button_pi = tk.Button(master=frame, text='π', padx=15, pady=5, width=3, command=lambda: myclick(math.pi))
button_pi.grid(row=10, column=1, pady=2)
button_pi.grid_remove()

button_e = tk.Button(master=frame, text='e', padx=15, pady=5, width=3, command=lambda: myclick(math.e))
button_e.grid(row=10, column=2, pady=2)
button_e.grid_remove()

window.mainloop()
