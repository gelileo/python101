class Car:
  def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

  def display_info(self):
      print(f"{self.year} {self.make} {self.model}")


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2018)

print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Accord

car1.display_info()  # Output: 2020 Toyota Camry
car2.display_info()  # Output: 2018 Honda Accord


class ElectricCar(Car):
  def __init__(self, make, model, year, battery_capacity):
      super().__init__(make, model, year)
      self.battery_capacity = battery_capacity

  def display_battery_info(self):
      print(f"Battery Capacity: {self.battery_capacity} kWh")
