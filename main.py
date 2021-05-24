import json
import random
print("test")
with open('qoutes.json', 'r') as file:
    x = json.load(file)

xyz = random.randint(1, len(x))

print(f"{x[xyz]['quote']} \n- {x[xyz]['author']}")
