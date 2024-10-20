
# def add(a, b):
#   return a + b

# def subtract(a, b):
#   return a - b

# def divide(a, b):
#   return a / b

# def multiply(a, b):
#   return a + b

# from my_moduel import *
# from my_moduel import add, subtract, divide, multiply
import my_moduel

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
      print("Please enter 1/2/3/4:")

def calculate(operation):
  while True:

      if operation == 1:
        # result = add(num1, num2)
        # print(result)
        print(my_moduel.add(num1, num2))
        break
      elif operation == 2:
        print(sth)
        print(my_moduel.subtract(num1, num2))
        break

      elif operation == 3:
        print(my_moduel.multiply(num1, num2))
        break

      elif operation == 4:
        print(my_moduel.divide(num1, num2))
        break
      else:
        print("please enter 1/2/3/4")


max_num_try = 3
i = 0
while i<=3:
    i += 1
    num1 = enter_a_num("Enter first number: ")
    num2 = enter_a_num("Enter second number: ")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = enter_op("Enter the operation: ")
    try:
      calculate(operation)
      break
    except ZeroDivisionError as e:
      print(e)
      # continue
    except: 
      print("an error occurred")
      # continue


   # finally:
   #    print("encounter an error!")


"""
Returns False when it gets wrong input
"""


if i>3:
  print("Omg, you're dumb!")
else:
  print("Adios!")