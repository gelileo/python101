
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
