userAge = input("how old are you? ")
age = int(userAge)
#Ask Age

if age > 18 and age < 65:
  # print("You're hired")
  ab = input("Can you swim? Y/N ")
  #Can you swim
  if ab == ("Y"):
    print("Wonderful!")
    if ab == ("Y"):
      a = input("How many years have you swam for? ")
      a = int(a)
      if a > 2:
        print("Great!")
      else:
        print("Bye, have a good day!")
  if ab == ("N"):
    print("Go Away")
elif age <= 18:
  print("Sorry, you're too young")
else:
  print("Sorry, you're too old")


