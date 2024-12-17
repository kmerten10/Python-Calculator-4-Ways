#Using while loops for immediate feedback & "re-prompting"
while True:
    operand = input("Number 1: ")
    try:
        operand = float(operand)
        break
    except:
        print("Invalid number, try again.")
        
while True:
    operand2 = input("Number 2: ")
    try:
        operand2 = float(operand2)
        break
    except:
        print("Invalid number, try again")
        
sign = input("Sign: ")

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
else:
    print("Invalid sign")

print(result)
