# Error handling in Python allows you to manage runtime errors gracefully and prevent your program from crashing unexpectedly. Python uses exceptions to indicate that an error has occurred, and you can handle these exceptions using the try, except, else, and finally blocks.

# Key Components of Error Handling

#   1.	try Block:
# The code that might raise an exception is placed in the try block. Python will attempt to execute this block.
#   2.	except Block:
# This block runs if an exception is raised in the try block. You can specify the type of exception to handle, or use a general except block to catch all exceptions.
#   3.	else Block (Optional):
# If no exceptions occur, the code in the else block will execute. This block is used for code that should run if everything in the try block worked fine.
#   4.	finally Block (Optional):
# Code in the finally block will always run, regardless of whether an exception was raised or not. It’s typically used for cleanup actions, like closing files or network connections.

# Basic Example of Error 
## Example 1: Handling Division by Zero
try:
  # Try to perform division
  result = 10 / 0
except ZeroDivisionError:
  # Handle the exception if division by zero occurs
  print("Error: Cannot divide by zero!")
else:
  # If no exception occurs, print the result
  print(f"Result: {result}")
finally:
  # This block will always run
  print("Execution completed.")


# Common Exception Types

# Here are some common exceptions you might encounter:

#   •	ZeroDivisionError: Raised when division by zero is attempted.
#   •	ValueError: Raised when a function receives an argument of the correct type but inappropriate value (e.g., trying to convert a string to an integer that cannot be converted).
#   •	TypeError: Raised when an operation or function is applied to an object of inappropriate type.
#   •	FileNotFoundError: Raised when an attempt to open a file that does not exist is made.
#   •	IndexError: Raised when trying to access an index that is out of bounds for a list or tuple.



## Example 2: Handling Multiple Exceptions
try:
  # Try to perform division and convert input
  num = int(input("Enter a number: "))
  result = 10 / num
except ZeroDivisionError:
  print("Error: Cannot divide by zero!")
except ValueError:
  print("Error: Invalid input! Please enter a valid integer.")
else:
  print(f"Result: {result}")
finally:
  print("Execution completed.")


## Example 3: Manually Raising an Exception

def check_positive_number(num):
  if num < 0:
      raise ValueError("Number must be positive!")
  return num

try:
  num = int(input("Enter a positive number: "))
  check_positive_number(num)
  print(f"You entered: {num}")
except ValueError as ve:
  print(f"Error: {ve}")


# Using finally for Cleanup

# The finally block is especially useful for tasks like cleaning up resources, closing files, or terminating network connections.

## Example 4: Closing Files in the finally Block
try:
  file = open("example.txt", "r")
  content = file.read()
  print(content)
except FileNotFoundError:
  print("Error: File not found!")
finally:
  # Ensure the file is closed no matter what happens
  if 'file' in locals() and not file.closed:
      file.close()
      print("File closed.")

# Catching All Exceptions

# You can use a bare except block to catch any kind of exception, but this is generally not recommended because it can hide errors and make debugging harder.

## Example 5: Catching All Exceptions (Not Recommended)
try:
  # Try some operation
  result = 10 / 0
except:
  # Catch any type of exception
  print("An error occurred.")

# Custom Exceptions

# You can create your own custom exceptions by subclassing the built-in Exception class.

## Example 6: Creating a Custom Exception
# Define a custom exception class
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: {value} is a negative number!")

# Function that raises the custom exception
def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    return num

try:
    num = int(input("Enter a positive number: "))
    check_positive_number(num)
    print(f"You entered: {num}")
except NegativeNumberError as ne:
    print(ne)