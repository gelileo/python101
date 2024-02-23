jamie = {"type": "Dog",
   "say": "moo",
   "num_of_legs": 4,
   "can_run": True,
   "can_fly": True,
   "hobby": "fly",
   "name": "jamie"
   }

bob = {"type": "Cat",
 "say": "onik",
 "num_of_legs": 6,
 "can_run": False,
 "can_fly": True,
 "hobby": "nap",
 "name": "bob"
 }

molly = {"type": "Duck",
   "say": "woof",
   "num_of_legs": 7,
   "can_run": False,
   "can_fly": False,
   "hobby": "scammer",
   "name": "molly"
   }

peaches = {"type": "Fish",
     "say": "oohoohahah",
     "num_of_legs": 30,
     "can_run": True,
     "can_fly": True,
     "hobby": "hunting",
     "name": "peaches"
     }

animals = [jamie, bob, molly, peaches]

def leg_cnt_animals_can_fly():
  flying_animals = [animal for animal in animals if animal["can_fly"] == True]
  total_fly = sum(animal["num_of_legs"] for animal in flying_animals)
  print(f"Total: {total_fly}")

leg_cnt_animals_can_fly()

# print out
# - names of animal can run
# - names of animals can fly
# - names of animals who has odd number of legs
# def summary():



