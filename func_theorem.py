import json
import datetime
import random

with open("theorems.json", "r", encoding="utf-8") as f:
    theorems = json.load(f)

def get_theorem_of_the_day():
    today_str = datetime.date.today().isoformat()  # "2026-03-24"
    index = hash(today_str) % len(theorems)
    return theorems[index]

def get_random_theorem():
    return random.choice(theorems)

print(get_theorem_of_the_day())
print(get_random_theorem())