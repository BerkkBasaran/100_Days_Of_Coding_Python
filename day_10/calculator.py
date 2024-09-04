# number = []
# calculation_signs = ["+", "-", "*", "/"]
# total_calculation = 0
# use_previous = True

# def calculation_step(number_input, sign_input, number_input_other):
#     number_input = int(input("What is the first number?: "))
#     for i in range(0,4):
#         print(calculation_signs[i]) 
#     sign_input = input("Pick an operation: ")
#     number_input_other = int(input("What is the next number?: "))
#     total_calculation = number_input + sign_input + number_input_other
#     return f"{number_input} {sign_input} = {total_calculation}"

# def yes_no():
#     decision = input(f"Type 'y' to continue calculation with {total_calculation}, or type 'n' to start a new calculation: ").lower()
#     if decision == "no":
#         use_previous = False
#         total_calculation = 0
    

# while use_previous:
import art

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiple(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" : divide
}
def calculator():
    should_accumulate = True
    print(art.calculator_logo)
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1,num2) 
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choise = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ").lower()

        if choise == "y":
            num1 = answer
        else: 
            should_accumulate = False
            print("\n"*40)
            calculator()

calculator()