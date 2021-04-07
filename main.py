# -*- coding: utf-8 -*-
from art import logo
from replit import clear
import operator

def calculator():
    clear()
    print(logo)
    firstNumber = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")
    continue_calc = True

    while continue_calc is True:
        selectedMathOperator = input("Pick an operation: ")
        secondNumber = float(input("What's the second Number?: "))
        mathOperators = {
            "+": operator.add(firstNumber, secondNumber),
            "-": operator.sub(firstNumber, secondNumber),
            "*": operator.mul(firstNumber, secondNumber),
            "/": operator.floordiv(firstNumber, secondNumber),
            }
        if selectedMathOperator in mathOperators:
            result = mathOperators[selectedMathOperator]
            print(f"{firstNumber} {selectedMathOperator} {secondNumber} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            firstNumber = result
        else:
            continue_calc = False
            calculator()

calculator()