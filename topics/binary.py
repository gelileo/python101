
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)
    return binary_num[2:]  # Remove the '0b' prefix

# decimal_num = int(input("Enter a decimal number: "))
# binary_num = decimal_to_binary(decimal_num)
# print(f"Binary representation: {binary_num}")

def binary_to_decimal(binary_str):
    decimal_num = int(binary_str, 2)
    return decimal_num

# binary_str = input("Enter a binary number: ")
# decimal_num = binary_to_decimal(binary_str)
# print(f"Decimal representation: {decimal_num}")


    1
+   2
-----
    3


    9
+   1
------
   10     1 *  10  + 0

   11     1 * 10 + 1

   34     3 * 10 + 1

23456     2 * 10,000 + 3 * 1,000 + 4 * 100 + 5 * 10 + 6 * 10^0

43210     2 * 10 ^ 4 + 3 * 10 ^3 + 4 * 10^2 + 5 * 10^1 + 6 * 10^0


   binary

   1
+  0
------
   1

    1
+   1
-----
   10

    11
+    1
------
   100    

   0 1 10 11 100 101 110 111 1000
   0 1 2   3  4    5   6  7   8

   111

   2 1 0
   
   1 * 2 ^ 2 + 1 * 2 ^ 1 +  1* 2 ^0
     4       +   2       +   1  = 7

110 

   1 * 2 ^ 2 + 2* 2^1 + 0 = 6



