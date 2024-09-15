from typing import Protocol

class Greetable(Protocol):
    def greetings(self) -> str:
      pass

class Christmas:
    def greetings(self) -> str:
      return "Merry Christmas"

class Newyear:
    def greetings(self) -> str:
      return "Happy New Year"

def greet(seasonals: [Greetable], name: str) -> None:
    greetings = ' and '.join([holiday.greetings() 
                              for holiday in seasonals])
    print(f"{greetings} {name}!")

greet([Christmas(), Newyear()], "Leo")

