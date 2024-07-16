
def addition(num1, num2):
    return num1 + num2

def division(num1, num2):
    return num1 / num2

def subtraction(num1, num2):
    return num1 - num2

def multplication(num1, num2):
    return num1 * num2

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter Second number: "))
operator = input("Enter an operator('+', '/', '-', '*'): ")

if operator == "+":
    result = addition(num_1, num_2)
    print(result)
elif operator == "-":
    result = subtraction(num_1, num_2)
    print(result)
elif operator == "/":
    result = division(num_1, num_2)
    print(result)
elif operator == "*":
    result = multplication(num_1, num_2)
    print(result)
else:
    print("kindly check your input")

