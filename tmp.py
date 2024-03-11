from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json

@dataclass_json
@dataclass
class Address:
    street: str
    city: str

@dataclass_json
@dataclass
class Person:
    name: str
    age: int
    address: Address

# Create instances of nested classes
address = Address("123 Main St", "Cityville")
person = Person("John", 30, address)

# Convert the instance to JSON
json_data = person.to_json()

print(json_data)
