# import sys
# print(sys.path)

# to run, go to parent directory
#  python3 -m topics.str_format
from utils.util import demo

###
def basic():
    name = "Alice"
    age = 30
    formatted = "My name is {} and I am {} years old.".format(name, age)
    print(formatted)  # Output: "My name is Alice and I am 30 years old."

demo(basic, "Base String Replacement")

###
def named():
    name = "Bob"
    age = 25
    formatted = "My name is {person_name} and I am {person_age} years old.".format(person_name=name, person_age=age)
    print(formatted)  # Output: "My name is Bob and I am 25 years old."
demo(named, "Name Placeholder")

### 
def pos_and_named():
    formatted = "My name is {0} and I am {person_age} years old.".format("Carol", person_age=35)
    print(formatted)  # Output: "My name is Carol and I am 35 years old."
demo(pos_and_named, "Positional and Named Placeholders")

###
def number():
    amount = 12345.6789
    formatted = "Amount: {:.2f}".format(amount)
    print(formatted)  # Output: "Amount: 12345.68"
demo(number, "Number Formatting")


###
def padding_align():
    text = "Hello"
    formatted = "Centered: {:^10}".format(text)
    print(formatted)  # Output: "Centered:   Hello   "
    text = "Python"
    formatted = "Right-aligned: {:>10}".format(text)
    print(formatted)  # Output: "Right-aligned:     Python"
    formatted = "Left-aligned: {:_<10}".format(text)
    print(formatted)  # Output: "Left-aligned: Python____"
demo(padding_align, "Padding and Alignment")

###
def other_base():
    value = 42
    binary = "Binary: {:b}".format(value)
    octal = "Octal: {:o}".format(value)
    hexadecimal = "Hex: {:x}".format(value)
    print(binary, octal, hexadecimal)  # Output: "Binary: 101010", "Octal: 52", "Hex: 2a"
demo(other_base, "Binary, Octal, Hexadecimal")


###
def date():
    from datetime import datetime
    date = datetime(2022, 11, 2)
    formatted = "Date: {:%Y-%m-%d}".format(date)
    print(formatted)  # Output: "Date: 2022-11-02"
demo(date, "Date Formatting")

###
def currency():
    price = 42.5
    formatted = "Price: ${:.2f}".format(price)
    print(formatted)  # Output: "Price: $42.50"
demo(currency, "Currency Formatting")


###
def scientific():
    value = 12345.6789
    formatted = "Value: {:.2e}".format(value)
    print(formatted)  # Output: "Value: 1.23e+04"
demo(scientific, "Scientific Notation")


###
def multiple_value():
    name = "Alice"
    age = 30
    formatted = "Name: {}, Age: {:02d}".format(name, age)
    print(formatted)  # Output: "Name: Alice, Age: 30"
demo(multiple_value, "Combining Multiple Formatted Values")


###
def conditional():
    score = 85
    result = "Pass" if score >= 60 else "Fail"
    formatted = "Result: {}".format(result)
    print(formatted)  # Output: "Result: Pass"
demo(conditional, "Conditional Formatting")


def boolean():
    is_true = True
    formatted = "Is it true? {}".format(is_true)
    print(formatted)  # Output: "Is it true? True"
    formatted = "Is it true? {}".format("Yes" if is_true else "No")
    print(formatted)  # Output: "Is it true? Yes"
demo(boolean, "Boolean Formatting")


###
def dictionary():
    person = {"name": "Bob", "age": 25}
    formatted = "Name: {name}, Age: {age}".format(name=person["name"], age=person["age"])
    print(formatted)  # Output: "Name: Bob, Age: 25"
demo(dictionary, "Dictionary Formatting")


###
def special_char():
    text = "This is a \n newline"
    formatted = "Text: {!r}".format(text)
    print(formatted)  # Output: "Text: 'This is a \\n newline'"
demo(special_char, "Special Character Formatting")