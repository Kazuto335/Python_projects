logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
# Calculator
# ADD
def add(n1, n2):
    return n1 + n2
# SUB
def sub(n1, n2):
    return n1 - n2
# MUL
def mul(n1, n2):
    return n1 * n2
# DIV
def div(n1, n2):
    return n1 / n2
    
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
# Here i use OS module to create a clear screen fun. 
import os
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
repeat = True
while repeat : 
    num1 = int(input("whats the first number? : "))
    repeat1 = True
    while repeat1:
        num2 = int(input("whats the second number? : "))

        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an opration from the line avobe: ")
        answer = operations[operation_symbol](num1 , num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        

        more = input(f"Do you want performe more operation on {answer}. if YES then type'y' either 'n' for NO and 'c' for clear screeen and begien new calculation.").lower()
        if more == "y":
            repeat1 = True
            num1 = answer 
        if more == "c":
            repeat1 = False
            screen_clear()
        if more == "n":
            repeat = False
            repeat1 = False
 
        
