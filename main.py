import tkinter as tk
import sys, os
from tkinter import *

display_equation = ""

#Function to check which operator is called, and hence what function should be called as a result
def calculation(operator, num1, num2):
    if operator == "+":
        result = addition(num1, num2)

    elif operator == "-":
        result = subtraction(num1, num2)

    elif operator == "*":
        result = multiplication(num1, num2)

    elif operator == "/":
        result = division(num1, num2)

    return result


#function that does addition calculation, and outputs an integer result
def addition(num1, num2):
    max_length = max(len(num1), len(num2))
    carry = 0
    result = ''
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    for digit in range(max_length -1, -1, -1):
        remainder = carry
        remainder += 1 if num1[digit] == '1' else 0
        remainder += 1 if num2[digit] == '1' else 0
        result = ('1' if remainder % 2 == 1 else '0') + result

        carry = 0 if remainder < 2 else 1

    if carry !=0:
        result = '1' + result

    final_result = binary_to_denary(result)

    return final_result

#function that does addition calculation, but outputs a binary result rather than integer, useful for use in the subtraction function as ouputs entire string
def addition2_forsubtraction(num1, num2):
    max_length = max(len(num1), len(num2))
    carry = 0
    result = ''
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    for digit in range(max_length -1, -1, -1):
        remainder = carry
        remainder += 1 if num1[digit] == '1' else 0
        remainder += 1 if num2[digit] == '1' else 0
        result = ('1' if remainder % 2 == 1 else '0') + result

        carry = 0 if remainder < 2 else 1

    if carry !=0:
        result = '1' + result

    final_output = result.zfill(max_length)
    return final_output[1:]

#function that carries out addition for the multiplcation function, as it only outputs full binary string rather than from second index
def addition3(num1, num2):
    max_length = max(len(num1), len(num2))
    carry = 0
    result = ''
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    for digit in range(max_length -1, -1, -1):
        remainder = carry
        remainder += 1 if num1[digit] == '1' else 0
        remainder += 1 if num2[digit] == '1' else 0
        result = ('1' if remainder % 2 == 1 else '0') + result

        carry = 0 if remainder < 2 else 1

    if carry !=0:
        result = '1' + result

    final_output = result.zfill(max_length)
    return final_output

#subtraction function that carries out binary subtraction using help from other helper functions
def subtraction(num1, num2):
    leftmost_bit = '1'
    num2_negative = leftmost_bit + num2
    max_length = max(len(num1), len(num2_negative))
    num1 = num1.zfill(max_length)
    num2_negative = num2_negative.zfill(max_length)

    num2_list = [*num2_negative]

    for digit in range(0, len(num2_list)):
        if num2_list[digit] == '0':
            num2_list[digit] = '1'
        else:
            num2_list[digit] = '0'

    num2_back = ''.join(digit for digit in num2_list)

    new_num2_final = addition2_forsubtraction(num2_back, '0001')

    max_length2 = max(len(num1),len(new_num2_final))

    num1_final = num1.zfill((max_length2))
    num2_final = new_num2_final.zfill((max_length2))

    subtraction_complete = addition2_forsubtraction(num1_final, num2_final)

    if subtraction_complete[0] == '1':
        final_subtraction = "- " + str(binary_to_denary(subtraction_complete[1:]))
    else:
        final_subtraction = binary_to_denary(subtraction_complete)

    return final_subtraction

#function that carries out binary multiplication using helper functions created earlier
def multiplication(num1, num2):
    result = "0"

    for i in range(len(num2) - 1, -1, -1):
        if num2[i] == "1":
            result = addition3(result, num1)

        num1 = num1 + "0"

    final_multiplication = binary_to_denary(result)
    return final_multiplication

#binary division function, but no solution :(
def division(num1, num2):
    return "solution unavailable"

#function that seperates the input provided within the calculator to seperate the first provided integer, operator and the seocnd provided integer
def separate_equation(equation2):
    # Initialize variables to store integers and operator
    num1 = ""
    num2 = ""
    operator = None

    # Iterate through each character in the equation
    for char in equation2:
        # Check if the character is a digit
        if char.isdigit():
            if not operator:
                # If operator is not set, append to num1
                num1 += char
            else:
                # If operator is set, append to num2
                num2 += char
        else:
            # If the character is not a digit, it is the operator
            operator = char

    # Convert the extracted strings to integers
    num1 = int(num1)
    num2 = int(num2)

    num1_final = convert_to_binary(num1)
    num2_final = convert_to_binary(num2)

    result = calculation(operator, num1_final, num2_final)

    return result

#function that converts any integer into a binary number
def convert_to_binary(num):
    int_array = []
    number_in_binary = ""

    while num > 0:
        val = num%2
        int_array.append(val)
        num = num // 2

    for i in range(0,len(int_array)):
        int_array[i] = str(int_array[i])

    final_string = number_in_binary.join(int_array[::-1])

    return final_string

#function that converts any binary strinbg into a integer
def binary_to_denary(num):
    num_int = str(num)
    return int(num_int,2)


#function that displays what is currently assigned to the display_equation variable within the tkinter package
def show(value):
    global display_equation
    display_equation += value
    text_result.config(text = display_equation)

#function that sets the display_equation variable to null
def clear():
    global display_equation
    display_equation = ""
    text_result.config(text = display_equation)

#function that calls all of the function and returns the output when the "=" sign is clicked
def calculate():
    global display_equation
    result = ""
    if display_equation != "":
        result = separate_equation(display_equation)

    text_result.config(text = result)

#Graphical User interface set up
root = Tk()
root.title("Binary Calculator")
root.geometry("570x550+100+200")
root.resizable(False,False)
root.configure(bg = "#17161b")

text_result = Label(root, width = 40, height = 2, text = "", font = ("Times New Roman",30))
text_result.pack()

#Code for all the buttons, and assigned lambda functions so they all have a function
Button(root, text = "C", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda:clear()).place(x=10, y= 100)
Button(root, text = "/", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("/")).place(x=150, y= 100)
Button(root, text = "+", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("+")).place(x=290, y= 100)
Button(root, text = "*", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("*")).place(x=430, y= 100)

Button(root, text = "7", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("7")).place(x=10, y= 200)
Button(root, text = "8", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("8")).place(x=150, y= 200)
Button(root, text = "9", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("9")).place(x=290, y= 200)
Button(root, text = "-", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("-")).place(x=430, y= 200)

Button(root, text = "4", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("4")).place(x=10, y= 300)
Button(root, text = "5", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("5")).place(x=150, y= 300)
Button(root, text = "6", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("6")).place(x=290, y= 300)

Button(root, text = "1", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("1")).place(x=10, y= 400)
Button(root, text = "2", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("2")).place(x=150, y= 400)
Button(root, text = "3", width = 5 , height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("3")).place(x=290, y= 400)

Button(root, text = "0", width = 24, height = 1, font = ("Times New Roman",30,"bold"), bd = 1, fg = "#2a2d36", bg = "#fff", command = lambda: show("0")).place(x=10, y= 480)
Button(root, text = "=", width = 5, height = 6, font = ("Times New Roman",30,"bold"), bd = 1,  fg = "#2a2d36", bg = "#fff", command = lambda: calculate()).place(x=430, y= 300)

root.mainloop()




