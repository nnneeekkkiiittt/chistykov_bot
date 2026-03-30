import json
import datetime
import random
import requests
import os
from google import genai

with open("theorems.json", "r", encoding="utf-8") as f:
    theorems = json.load(f)

#GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")
GIGACHAT_URL = "https://gigachat.devices.sberbank.ru/"
GEMINI_API_KEY = os.getenv('GEMINI_TOKEN')

def ask(prompt: str):
    client = genai.Client()

    response = client.models.generate_content(model="gemini-3-flash-preview", contents = 'Представь, что ты - возрастной профессор высшей математики в НИУ ВШЭ. ответь студенту мудро и по философски на его вопрос, используя максимум 200 символов: ' + prompt)
    return response.text

def get_theorem_of_the_day():
    today_str = datetime.date.today().isoformat()
    index = hash(today_str) % len(theorems)
    return theorems[index]

def get_random_theorem():
    return random.choice(theorems)

print(get_theorem_of_the_day())
print(get_random_theorem())