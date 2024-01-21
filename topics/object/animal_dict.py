# Define individual animals as dictionaries
dog = {"name": "Charlie", "type": "Dog", "can_run": True, "can_swim": False, "can_fly": False}
cat = {"name": "Whiskers", "type": "Cat", "can_run": True, "can_swim": False, "can_fly": False}
cow = {"name": "Molly", "type": "Cow", "can_run": True, "can_swim": False, "can_fly": False}
duck = {"name": "Donald", "type": "Duck", "can_run": False, "can_swim": True, "can_fly": True}

# Function to mimic the say() method
def say(animal):
    sounds = {"Dog": "Woof!", "Cat": "Meow!", "Cow": "Moo!", "Duck": "Quack!"}
    return sounds.get(animal['type'], "Unknown sound")

# Functions to check abilities
def can_run(animal):
    return animal.get("can_run", False)

def can_swim(animal):
    return animal.get("can_swim", False)

def can_fly(animal):
    return animal.get("can_fly", False)

# List of animals
animals = [dog, cat, cow, duck]

# Test the functionality
for animal in animals:
    print(f"The {animal['type']} named {animal['name']} says {say(animal)}")
    print(f"Can run: {can_run(animal)}")
    print(f"Can swim: {can_swim(animal)}")
    print(f"Can fly: {can_fly(animal)}\n")
