import json
import random

with open('qoutes.json', 'r') as file:
    x = json.load(file)

xyz = random.randint(1, 1000)

print(f"{x[xyz]['quote']} \n- {x[xyz]['author']}")
