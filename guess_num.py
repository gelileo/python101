import random
# generate random number 1-20
number = random.randint(1, 20)
# print(number)

# let user enter a number
userInput = int(input("Make a guess between 1 and 20:"))

# print("user entered: " + userInput)

# until it's right
# if it too big, let try a smaller 

notCorrect = True

while notCorrect:
  if userInput > number:
    userInput = int(input("Try a smaller number: "))
  elif userInput < number:
    userInput = int(input("Try a bigger number: "))
  else:
    print("Good job!!")
    notCorrect = False



print("this is game over!!")


