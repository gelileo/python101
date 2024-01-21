# Define the base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def say(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def can_run(self):
        return False

    def can_swim(self):
        return False

    def can_fly(self):
        return False

# Define subclasses for Dog, Cat, Cow, and Duck
class Dog(Animal):
    def say(self):
        return "Woof!"

    def can_run(self):
        return True

class Cat(Animal):
    def say(self):
        return "Meow!"

    def can_run(self):
        return True

class Cow(Animal):
    def say(self):
        return "Moo!"

    def can_run(self):
        return True

class Duck(Animal):
    def say(self):
        return "Quack!"

    def can_swim(self):
        return True

    def can_fly(self):
        return True

# Create instances of each animal
charlie = Dog("Charlie")
whiskers = Cat("Whiskers")
molly = Cow("Molly")
donald = Duck("Donald")

# Test the functionality
animals = [charlie, whiskers, molly, donald]

# Filter animals by their ability
def filter_animals_by_ability(animals, ability):
    return [animal for animal in animals if ability(animal)]

# Define the abilities
abilities = {
    "can run": lambda animal: animal.can_run(),
    "can swim": lambda animal: animal.can_swim(),
    "can fly": lambda animal: animal.can_fly(),
}

# Test the filtering
for ability, func in abilities.items():
    able_animals = filter_animals_by_ability(animals, func)
    print(f"Animals that {ability}: {[animal.name for animal in able_animals]}")


for animal in animals:
    print(f"{animal.name} says {animal.say()}")