class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def says(self):
    print("I'm talking now")

  def howOldAreYou(self):
    print(f"I am {self.age} year old")


class Dog(Animal):
  def says(self):
    print("Woof")


class Cat(Animal):
  def says(self):
    print("Meow")




dog = Dog(name="peaches", age=1)
dog.says()

cat = Cat(name="cathy", age=2)
cat.says()

cat.howOldAreYou()
cat.age = dog.age
cat.howOldAreYou()




# person = {
#   "name": "adam",
#   "age": 15,
#   "height": "11 ft",
#   "contacts": {
#     "mobile": "717-222-1234",
#     "work": "717-333-1234",
#     "home": "717-444-1234",
#     "weChat #": "from-hershey",
#     "email": "sb@hms.com"
#   },
#   "address": {
#     "street": "321 lollypop Dr",
#     "city": "Dayton",
#     "state": "OH",
#     "country": "US",
#     "zip": "17033"
#   }
# }

# # get the mobil #

# for phone, contact in person["contacts"].items():
#   print(f"{phone}:{contact}")


# person["name"] = "Bob"
# print(person)

# # person["nickname"] = "Bobby"
# # print(person)
# person2 = {
#   "nickname": "Bobby",
#   "ssn": "111-11-1111",
#   "title": "Dr."
# }


# bob = person | person2
# print(bob)