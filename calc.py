# im just using slang guys

from sys import exit
import math

def calcPrgm():
    num1 = int(input("Enter number 1: "))
    operation = input("Enter in your operation (+, -, *, /, exp, power, square root, sin, cos, tan, log e) or press CTRL+C to exit: ")
    if operation != "exp":
        if operation != "square root":
            if operation != "sin":
                if operation != "cos":
                    if operation != "tan":
                        if operation != "log e":
                            num2 = int(input("Enter in number 2: "))

    # catching division by zero
    if operation == "/" and num2 == 0:
        exit("Cannot divide by zero.")

    # remove spaces from inputs
    operation = operation.replace(" ", "")

    if operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "/":
        print(num1/num2)
    elif operation == "exp":
        print(f"Exponential e of {num1} is {math.exp(num1)}")
    elif operation == "squareroot":
        print(math.sqrt(num1))
    elif operation == "power":
        print(pow(num1, num2))
    elif operation == "sin":
        print(math.sin(num1))
    elif operation == "cos":
        print(math.cos(num1))
    elif operation == "tan":
        print(math.tan(num1))
    elif operation == "loge":
        if num1 <= 0:
            print("undefined")
        else:
            print(math.log(num1))
    else:
        print("Invalid operation.")

while True:
    try:
        calcPrgm()
        print("\n")
    except KeyboardInterrupt:
        print("\nExitting.")
        exit()
    except Exception as e:
        print(e)