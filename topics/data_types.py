# Example vars
var1 = 42
var2 = "Hello, Python!"
var3 = 1.23
var4 = True
var5 = [1, 2, 3]
var6 = {"name": "John", "age": 30}

# Checking the types
type_of_var1 = type(var1)
type_of_var2 = type(var2)
type_of_var3 = type(var3)
type_of_var4 = type(var4)
type_of_var5 = type(var5)
type_of_var6 = type(var6)

# Printing the results
print(f"The type of var1 is {type_of_var1}")
print(f"The type of var2 is {type_of_var2}")
print(f"The type of var3 is {type_of_var3}")
print(f"The type of var4 is {type_of_var4}")
print(f"The type of var4 is {type_of_var5}")
print(f"The type of var4 is {type_of_var6}")


def get_type_name(value):
  # Get the type using type() and convert it to a string
  type_str = str(type(value))
  # Extract the type name between single quotes
  type_name = type_str.split("'")[1]
  return type_name


print(f"The type of var1 is {get_type_name(var1)}")
print(f"The type of var1 is {get_type_name(var2)}")
print(f"The type of var1 is {get_type_name(var3)}")
print(f"The type of var1 is {get_type_name(var4)}")
print(f"The type of var1 is {get_type_name(var5)}")
print(f"The type of var1 is {get_type_name(var6)}")
