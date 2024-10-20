## Lesson 3 Fibonacci
## a sequence in which each number is the sum of the two preceding ones. 

# fib = [1,1,2,3]
# n: the length of the returned sequence
# return a list of Fibonacci numbers
def fib(n, debug=False):
  ret = [] # starting values
  i,j = 0,1

  if debug:
    print(f"Entering Loop: {ret}. i:1, j:1")
  for a in range(n): # do it for n numbers
    ret.append(j)
    j += i # new j is old j + old i
    i = j - i # new i is old j or new j - old i
    if debug:
      print()
      print(f"Iteration({a}): ")
      print(f"{ret}, i:{i}, j:{j})")
    
  return ret[:] # return the list

# print("Here's my Fibonacci Numbers:")
# print(fib(0))


test_cases = [[],
            [1],
            [1,1],
            [1,1,2],
            [1,1,2,3],
            [1,1,2,3,5],
            [1,1,2,3,5,8]]

def testFib(n):
  if fib(n) == test_cases[n]:
    print(f"fib({n}) passed!")
  else:
    print(f"fib({n}) failed!")

def test():
  testFib(0)
  testFib(1)
  testFib(2)
  testFib(5)
  testFib(6)

test()

print(fib(5))
def review_list():
  list = [0,1,2,3,4,5]
  
  print(list[0]) # print the first element of the list
  print(list[0:2]) # print elements in a range
  
  print(list[-1]) # print last element
  
  list.remove(5) # remove the element with value 5
  print(list)
  
  list.append(5) # append an element with value 5
  print(list)
  
  print(list.pop())  # removes and returns the last element
  print(list)