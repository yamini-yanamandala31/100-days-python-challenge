import random

subjects = ["Yamini", "A dog", "A teacher", "A hacker"]
actions = ["eating", "playing with", "running after", "building"]
objects = ["a pizza", "a laptop", "a car", "a robot"]
places = ["in Hyderabad", "at school", "on the moon", "in a park"]

print("Your Random Story 😂👇\n")

print(random.choice(subjects),
      random.choice(actions),
      random.choice(objects),
      random.choice(places))
