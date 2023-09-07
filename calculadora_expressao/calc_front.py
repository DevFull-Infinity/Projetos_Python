import tkinter as tk
from tkinter import StringVar,ttk
from motor import *

expr = ' '

def On_click(char):
    global expr

    operacoes = ["+","-","x","÷"]

    if char in operacoes and expr[-1] in operacoes:
        expr = expr.replace(expr[-1],char)
        display.set(expr)


    elif char != "=" and char !="C":
        expr += char
        display.set(expr)
    
    
    elif char == "C":
        display.set('')
        expr = ' '

    else:
        expr = expr.replace("÷","/")
        expr = expr.replace("x","*")
        expr = expr.replace(",",".")
        display.set(resolvedor("".join(expr[0:].split())))
        

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x550")
root.resizable(False,False)


temp = StringVar()
display = StringVar()

texto = ttk.Label(root,textvariable=display, background="gray",width=62)
texto.grid(row =0, column= 0, columnspan=5)

btn0 = ttk.Button(root, text = "0", command= lambda:On_click('0'), width=37)
btn1 = ttk.Button(root, text = "1", command= lambda:On_click('1'))
btn2 = ttk.Button(root, text = "2", command= lambda:On_click('2'))
btn3 = ttk.Button(root, text = "3", command= lambda:On_click('3'))
btn4 = ttk.Button(root, text = "4", command= lambda:On_click('4'))
btn5 = ttk.Button(root, text = "5", command= lambda:On_click('5'))
btn6 = ttk.Button(root, text = "6", command= lambda:On_click('6'))
btn7 = ttk.Button(root, text = "7", command= lambda:On_click('7'))
btn8 = ttk.Button(root, text = "8", command= lambda:On_click('8'))
btn9 = ttk.Button(root, text = "9", command= lambda:On_click('9'))
btn_sum = ttk.Button(root, text = "+", command= lambda:On_click('+'))
btn_sub = ttk.Button(root, text = "-", command= lambda:On_click('-'))
btn_mult = ttk.Button(root, text = "x", command= lambda:On_click('x'))
btn_div = ttk.Button(root, text = "÷", command= lambda:On_click('÷'))
btn_igual = ttk.Button(root, text = "=", command= lambda:On_click('='))
btn_clear = ttk.Button(root, text = "C", command= lambda:On_click('C'))
btn_modulo = ttk.Button(root, text = "%", command= lambda:On_click('%'))
btn_ponto = ttk.Button(root, text = ",", command= lambda:On_click(','))

btn7.grid(row =3, column= 0)
btn8.grid(row =3, column= 1)
btn9.grid(row =3, column= 2)
btn4.grid(row =4, column= 0)
btn5.grid(row =4, column= 1)
btn6.grid(row =4, column= 2)
btn1.grid(row =5, column= 0)
btn2.grid(row =5, column= 1)
btn3.grid(row =5, column= 2)
btn0.grid(row =6, column= 0,columnspan=3)
btn_sum.grid(row =3, column= 3)
btn_sub.grid(row =3, column= 4)
btn_mult.grid(row =4, column= 3)
btn_div.grid(row =4, column= 4)
btn_igual.grid(row =5, column= 3)
btn_clear.grid(row = 5, column = 4)
btn_modulo.grid(row = 6, column = 3)
btn_ponto.grid(row = 6, column = 4)
root.mainloop()