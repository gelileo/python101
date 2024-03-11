import json

class Contact:
  def __init__(self, phone, email):
    self.phone = phone
    self.email = email
  
class Address:
  def __init__(self, street, city, state, zip):
    self.street = street
    self.city = city
    self.state = state
    self.zip = zip 


class Person: 
  def __init__(self, name, age, height, contact, address):
    self.name= name
    self.age= age
    self.height= height
    self.contact = contact
    self.address = address
    
  def to_dict(self):
    ret = self.__dict__
    ret['contact'] = self.contact.__dict__
    ret["address"] = self.address.__dict__
    return ret

contact1 = Contact("7171-111-1111", "blah@gmail.com")

address1 = Address("some st.", "Hershey", "PA", "17033")

dan = Person("Daniel", 12, "5'", contact1, address1)

chris = Person("Christine", 16, "5'", contact1, address1)

# print(dan.__dict__)

print(json.dumps(dan.address.__dict__, indent=4))

print(json.dumps(chris.to_dict(), indent=4))
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


# him = Person("joe", 44, "5'")
# print(json.dumps(him.__dict__,  indent=5))