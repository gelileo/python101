# while
# A simple while loop that prints numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1


# for
# A simple for loop that iterates through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# range
# Looping from 0 to 4 using range()
for i in range(5):
    print(i)


# Loop from 1 to 9, incrementing by 2
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

## Loop control
# Break out of the loop when i equals 3
for i in range(5):
    if i == 3:
        break
    print(i)

# Skip when i equals 3
for i in range(5):
    if i == 3:
        continue
    print(i)

# Skip even numbers and print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Output: 1, 3, 5, 7, 9
