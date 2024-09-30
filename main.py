# Error Handling
# num = 10
# num2 = 0

# try:
#   print(f"{num} divided by {num2} = {num/num2}")
# except ZeroDivisionError as e:
#   print(f"error: {e}")
# else:
#   print("some error")
  
# print(f"{num} added by {num2} = {num + num2}")

# define functions for 4 basic operation
# each takes two arguments
# ex: add(1,2) returns 3

def add(a, b):
  return a + b
  
def subtract(a, b):
  return a - b
  
def divide(a, b):
  return a / b
  
def multiply(a, b):
  return a + b


"""Ask the user to enter the numbers and desired operation. Our program performs the operation"""


"""
A func take a number input, and prompt user
to enter again until a valid input
Returns the integer
"""
def enter_a_num(message):
  while True:
    try:
       return float(input(message))
    except ValueError:
      print("Invalid input. Please try again")

def enter_op(message):
  while True:
    try:
      op = int(input(message))
      if op in [1,2,3,4]:
        return op
    except:
      print("Type operation")

def calculate84():
  while True:
    try:
    if operation == 1:
      print(add(num1, num2))
      break
    elif operation == 2:
      print(subtract(num1, num2))
      break

    elif operation == 3:
      print(multiply(num1, num2))
      break

    elif operation == 4:
      print(divide(num1, num2))
      break
    else:
      print("please enter 1/2/3/4")

    
  


"""
Returns False when it gets wrong input
"""
def old_run():

  if operation == '1':
    print(add(num1, num2))
    return True

  elif operation == "2":
    print(subtract(num1, num2))
    return True

  elif operation == "3":
    print(multiply(num1, num2))
    return True

  elif operation == "4":
    print(divide(num1, num2))
    return True
  else:
    print("please enter 1/2/3/4")

  i+=1
  return False

max_num_try = 3
i = 0
while i<=3:
  num1 = enter_a_num("Enter first number ")
  num2 = enter_a_num("Enter second number ")
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  operation = enter_op("ENter the opperation: ")
    
  
if i>3:
  print("Omg, you're dumb!")
else:
  print("Adios!")