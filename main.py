from re import X


list = [i for i in range(1,10)]
print(list)

# Output:
# 1 2 3
# 4 5 6 
# 7 8 9
#

list = ['X' for _ in range(9)]
print (list)
#  X | O | X
# ----------
#  O | X | O
# ----------
#  X | O | X





# list1 = [1,2,3,4,5,6,7,8,9,24, 636, 15, 3647]
# # print(f'list1: {list1}')

# list2 = [ i for i in range(1,10) if i<5]
# print(f'list2: {list2}')

# list3 = []
# for i in range(1,10):
#   if i < 5:
#     list3.append(i+100)

# print(f'list3: {list3}')


# ODD
# list2 = [i for i in list1 if i%2 != 0]
# print(f'list2: {list2}')


# print('-'*9)

# # arr = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
# arr = ['-' for _ in range(9)] # this gives you the same list

# print(len(arr))
# print(arr)
# for i in arr:
#   print(i, end='')
# print()



  



# arr = ['1','2','3']

# print(arr[0]) # 1
# print(arr[2]) # 3
# # print(arr[3]) # err: list index out of range

# arr.append('4')
# print(arr)

# arr[0] = '0'
# print(arr)


# # arr[4] = '5' # out of range
# arr.append('5')
# # print(arr)
# arr[4] = 'x'
# print(arr)