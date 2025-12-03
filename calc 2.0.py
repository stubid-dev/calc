def power():  
        while True:
            command=input("Enter command (Calculate/End):").strip().lower()
            if command=='calculate':
                calc()
            elif command=='end':
                print("Calculator power off")
                break
            else:
                print('invaild input. please try again')

def calc():
    print("CALCULATOR 1.4")
    print("current possible arithmetics: +,-,*,/,%")
            
    def number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid number. Please try again")
            
    num1= number("Enter 1st Number:")
    num2= number("Enter 2nd Number")
    op=input("op(+,-,*/):")
    while True:
            
        if op =="+":
            print(num1+num2)
            break
        elif op =="-":
            print(num1-num2)
            break
        elif op =="*":
            print(num1*num2)
            break
        elif op =="/":
            if num2==0:
                print("No number is divisable by zero")
                num2 = number("Enter 2nd Number again: ")  
                continue
            else:   
                print(num1/num2)
            break
        elif op == "%":
            if num2==0:
                print("dumbass")
            else:
                print(f"{num1} is {(num1/num2)*100}% of {num2}")
            break
        else:
            print("invalid op, try again")

power()

import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")

label = tk.Label(root, text= "nihao mf")
label.pack()

def click_me():
    label.config( text = "U clicked :)")

button = tk.Button(root, text = "click meee", command=click_me)
button.pack()

root.mainloop()
