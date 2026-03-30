import json
import datetime
import random
import requests
import os

with open("theorems.json", "r", encoding="utf-8") as f:
    theorems = json.load(f)

GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")
GIGACHAT_URL = "https://gigachat.devices.sberbank.ru/"

def ask(prompt: str):
    headers = {
        "Authorization": f"Bearer {GIGACHAT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": 'Представь, что ты - профессор высшей математики в университете. Ответь на следующий вопрос студента мудро и по философски: ' + prompt,
        "max_tokens": 200
    }
    response = requests.post(GIGACHAT_URL, json=data, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result.get("text", "")

def get_theorem_of_the_day():
    today_str = datetime.date.today().isoformat()
    index = hash(today_str) % len(theorems)
    return theorems[index]

def get_random_theorem():
    return random.choice(theorems)

print(get_theorem_of_the_day())
print(get_random_theorem())