# main.py

# Import everything from my_module
from my_module import *

# Now you can call all the functions and access variables directly
sum_result = add(10, 5)
pi_value = pi

print(f"Sum: {sum_result}")
print(f"Pi: {pi_value}")



# main.py

# Import the module and give it an alias
import my_module as utils

# Now use the alias to access functions and variables
sum_result = utils.add(10, 5)
pi_value = utils.pi

print(f"Sum: {sum_result}")
print(f"Pi: {pi_value}")



##

# Adding input validation with error handling

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter choice (1/2/3/4): ")

if operation == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif operation == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif operation == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif operation == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")

else:
    print("Invalid input, please choose a valid operation.")
