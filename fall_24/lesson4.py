## Lesson 4 Fibonacci with Tests
## a sequence in which each number is the sum of the two preceding ones.


def fib(n, debug=False):
    """
    Generate a Fibonacci sequence of length n. Ex: fib = [1,1,2,3] with n=4
    Args:
        n: the length of the returned sequence
        debug: print debug information
    Returns: a list of Fibonacci numbers
    """
    ret = []  # starting values
    i, j = 0, 1

    if debug:
        print(f"Entering Loop: {ret}. i:1, j:1")
    for a in range(n):  # do it for n numbers
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
    [1],
    [1, 1],
    [1, 1, 2],
    [1, 1, 2, 3],
    [1, 1, 2, 3, 5],
    [1, 1, 2, 3, 5, 8],
]


def test_fib(n):
    if fib(n) == test_cases[n]:
        print(f"fib({n}) passed!")
    else:
        print(f"fib({n}) failed!")


def test():
    test_fib(0)
    test_fib(1)
    test_fib(2)
    test_fib(5)
    test_fib(6)


test()

print(fib(5))


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
