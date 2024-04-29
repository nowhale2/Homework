import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def clear_input(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(value))


def add():
    num1, num2 = get_values()
    res = num1 + num2
    clear_input(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    clear_input(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    clear_input(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    clear_input(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", command=add)
button_add.place(x=100, y=80)
button_sub = tk.Button(window, text="-", command=sub)
button_sub.place(x=150, y=80)
button_mul = tk.Button(window, text='*', command=mul)
button_mul.place(x=200, y=80)
button_div = tk.Button(window, text='/', command=div)
button_div.place(x=250, y=80)
number1 = tk.Label(window, text='Введите первое число')
number1.place(x=100, y=25)
number1_entry = tk.Entry(window, width=27)
number1_entry.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число')
number2.place(x=100, y=125)
number2_entry = tk.Entry(window, width=27)
number2_entry.place(x=100, y=150)
equal_ = tk.Label(window, text='=')
equal_.place(x=175, y=200)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=250)
window.mainloop()
