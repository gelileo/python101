#Tea
tea_dict = {"a": "molihua tea",
           "b": "green tea",
           "c": "red tea",
           "d": "black tea",
           "e": "white tea"}

# print(tea_dict["a"])
# print(tea_dict["b"])
# print(tea_dict["c"])
# print(tea_dict["d"])
# print(tea_dict["e"])

for tea in tea_dict.values():
  print(tea)

print()

for key in tea_dict:
  print(key)
  print(tea_dict[key])

for key, value in tea_dict.items():
  print(f"{key}: {value}")

tea_dict["c"] = "yellow tea"

print()
for key, value in tea_dict.items():
  print(f"{key}: {value}")

person = {
  "name": "adam",
  "age": 15,
  "height": "11 ft",
  "contacts": {
    "mobile": "717-222-1234",
    "work": "717-333-1234",
    "home": "717-444-1234",
    "weChat #": "from-hershey",
    "email": "sb@hms.com"
  },
  "address": {
    "street": "321 lollypop Dr",
    "city": "Dayton",
    "state": "OH",
    "country": "US",
    "zip": "17033"
  }
}

# get the mobil #

for phone, contact in person["contacts"].items():
  print(f"{phone}:{contact}")


person["name"] = "Bob"
print(person)

# person["nickname"] = "Bobby"
# print(person)
person2 = {
  "nickname": "Bobby",
  "ssn": "111-11-1111",
  "title": "Dr."
}


bob = person | person2
print(bob)