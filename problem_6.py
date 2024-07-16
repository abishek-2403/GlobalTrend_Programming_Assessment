num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

try:
    result = num_1 / num_2
except ZeroDivisionError:
    print("Division by Zero! Try another number.")
else:
    print(f"The Answer is: {result}")