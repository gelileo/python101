## Lesson 4 Fibonacci with Tests
## a sequence in which each number is the sum of the two preceding ones.


# The Fibonacci sequence is a series of numbers where each number is
# the sum of the two preceding ones, starting from 0 and 1.
# Mathematically, it is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2)
# with initial conditions  F(0) = 0  and  F(1) = 1 .
#
def fib(n, debug=False):
    """
    Generate a Fibonacci sequence of length n. Ex: fib = [0, 1,1,2,3] with n=5
    Args:
        n: the length of the returned sequence
        debug: print debug information
    Returns: a list of Fibonacci numbers
    """
    ret = [0]  # starting values
    i, j = 0, 1

    if debug:
        print(f"Entering Loop: {ret}. i:0, j:1")
    for a in range(n - 1):  # do it for n numbers
        ret.append(j)
        j += i  # new j is old j + old i
        i = j - i  # new i is old j or new j - old i
        if debug:
            print()
            print(f"Iteration({a}): ")
            print(f"{ret}, i:{i}, j:{j})")

    return ret[:]  # return the list


test_cases = [
    [],
    [0],
    [0, 1],
    [0, 1, 1],
    [0, 1, 1, 2],
    [0, 1, 1, 2, 3],
    [0, 1, 1, 2, 3, 5],
    [0, 1, 1, 2, 3, 5, 8],
]


def test_fib(n, func=fib):
    if func(n) == test_cases[n]:
        print(f"fib({n}) passed!")
    else:
        print(f"fib({n}) failed!")


def test():
    test_fib(0)
    test_fib(1)
    test_fib(2)
    test_fib(3)
    test_fib(4)
    test_fib(5)
    test_fib(6)


test()


def review_list():
    my_list = [0, 1, 2, 3, 4, 5]

    print(my_list[0])  # print the first element of the list
    print(my_list[0:2])  # print elements in a range

    print(my_list[-1])  # print last element

    my_list.remove(5)  # remove the element with value 5
    print(my_list)

    my_list.append(5)  # append an element with value 5
    print(my_list)

    print(my_list.pop())  # removes and returns the last element
    print(my_list)


# def fib_simple(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return [0]

#     fib = [0, 1]
#     while len(fib) < n:
#         fib.append(fib[-1] + fib[-2])
#     return fib


# def fibonacci(n):
#     """
#     recursive version of the fibonacci function
#     Args:
#         n: the length of the returned sequence
#     Returns: a list of Fibonacci numbers
#     """
#     if n == 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib = fibonacci(n - 1)
#         fib.append(fib[-1] + fib[-2])
#     return fib
