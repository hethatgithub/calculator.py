from tkinter import *
import ast

root = Tk()

i = 0

def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    display.delete(0, END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

display = Entry(root, font=('Arial', 18))
display.grid(row=1, columnspan=6, sticky="nsew")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=5, height=2, font=('Arial', 18),
                        command=lambda text=button_text: get_number(text))
        counter += 1
        button.grid(row=x+2, column=y, sticky="nsew")

button = Button(root, text="0", width=5, height=2, font=('Arial', 18), command=lambda: get_number(0))
button.grid(row=5, column=1, sticky="nsew")

count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=5, height=2, font=('Arial', 18),
                            command=lambda text=operations[count]: get_operation(text))
            count += 1
            button.grid(row=x + 2, column=y + 3, sticky="nsew")

Button(root, text="AC", width=5, height=2, font=('Arial', 18), command=clear_all).grid(row=5, column=0, sticky="nsew")
Button(root, text="=", width=5, height=2, font=('Arial', 18), command=calculate).grid(row=5, column=2, sticky="nsew")
Button(root, text="<-", width=5, height=2, font=('Arial', 18), command=lambda: undo()).grid(row=5, column=4, sticky="nsew")

root.mainloop()
