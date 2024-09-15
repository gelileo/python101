# sum number from 1  to 5
# 1 + 2 + 3 +4 +5
# res = 1+2
# res = res + 3
# ...

# i=1
# result = 0
# while i < 50:
#   result += i
#   print(f"i= {i}, result: {result}")
#   i += 1

# print("the end ")

# find out the i when total reaches 100

i = 1
total = 0
# while i < 50 and total < 100:
#   total += i
#   print(f"i= {i}, total: {total}")
#   i += 1

# while i < 50:
#   total += i
#   print(f"i= {i}, total: {total}")
#   if total > 100:
#     break
#   i += 1

# a = [1,2,3,4,5, ...]
# r = range(1,50)
# for i in r:
#   total += i
#   print(f"i= {i}, total: {total}")
#   i += 1
#   if total > 100:
#     break

# print the total of the odd numbers and stop when total reaches 100



def check_odd(num):
  if (num % 2) != 0:
    return True
  else:
    return False

def check_even(num):
  return num % 2 == 0

# for i in range(1,15):
  # if check_odd(i):
  #   total += i
  # print(f"i= {i}, total: {total}")
  # if total >= 100:
  #   break
  # if check_odd(i):
  # if check_even(i) == False:
  #   print(i)

for i in range(1, 15, 3):
  print(i)




print("the end ")





# main.py

# Import everything from my_module
# from my_module import *

# # Now you can call all the functions and access variables directly
# sum_result = add(10, 5)
# pi_value = pi

# print(f"Sum: {sum_result}")
# print(f"Pi: {pi_value}")
