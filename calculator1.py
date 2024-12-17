#Using a boolean variable to determine validity before proceeding with calculations
operand = input("Number 1: ")
operand2 = input("Number 2: ")
sign = input("Sign: ")

valid = False
try:
    operand = float(operand)
    operand2 = float(operand2)
    valid = True
except:
    print("Invalid operand")

result = 0
if sign == "+":
    result = operand + operand
elif sign == "-":
    result = operand - operand2
elif sign == "/":
    if operand2 != 0:
        result = operand / operand
    else:
        print("Cannot divide by zero")
elif sign == "*":
    result = operand * operand
print(result)