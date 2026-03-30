import os
import re
from random import randint

from func_theorem import get_theorem_of_the_day
from func_theorem import get_random_theorem
from func_theorem import ask
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import json

with open("theorems.json", "r", encoding="utf-8") as f:
    theorems = json.load(f)

async def start(update: Update):
    await update.message.reply_text("Привет! Напиши 'теорема дня', и я пришлю сегодняшнюю теорему, или 'моя теорема', и я пришлю тебе, какая теорема ты сегодня!")

async def commands(update: Update):
    list_of_commands = 'Теорема дня: узнать сегодняшнюю теорему\nМоя теорема: узнать свою теорему\nМоя оценка: узнать свою оценку за матан\nВячеслав Васильевич, ...: спросить Вячеслава Васильевича о чем то (но обращайтесь правильно!)'

async def theorem_of_the_day(update: Update):
    text = update.message.text.lower()
    if "теорема дня" in text:
        theorem = get_theorem_of_the_day()
        await update.message.reply_text(f"Сегодняшняя теорема:\n{theorem['name']}\n{theorem['description']}")

async def random_theorem(update: Update):
    text = update.message.text.lower()
    if "моя теорема" in text:
        theorem = get_random_theorem()
        user_id = update.message.from_user.id
        user_name = update.message.from_user.first_name

        await update.message.reply_text(
            f'<a href="tg://user?id={user_id}">{user_name}</a>, твоя теорема:\n'
            f"{theorem['name']}\n{theorem['description']}",
            parse_mode="HTML")

async def marking(update: Update):
    text = update.message.text.lower()
    if "моя оценка" in text:
        user_id = update.message.from_user.id
        user_name = update.message.from_user.first_name
        await update.message.reply_text(
            f'<a href="tg://user?id={user_id}">{user_name}</a>, твоя оценка за матан:\n'
            f"{randint(0, 10)}",
            parse_mode="HTML")

async def asking(update: Update):
    text = update.message.text
    if 'Вячеслав Васильевич' in text:
        ans = ask(text)
        await update.message.reply_text(ans)

async def wrong_asking(update: Update):
    text = update.message.text.lower()
    if 'вячеслав васильевич' in text:
        await update.message.reply_text('Пошел нахуй')


if __name__ == "__main__":
    load_dotenv()
    app = ApplicationBuilder().token(os.getenv('TOKEN')).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(re.compile(r'моя теорема', re.IGNORECASE)), random_theorem))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(re.compile(r'теорема дня', re.IGNORECASE)), theorem_of_the_day))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(re.compile('моя оценка', re.IGNORECASE)), marking))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex('Вячеслав Васильевич'), asking))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(re.compile(r'вячеслав васильевич', re.IGNORECASE)), wrong_asking))


    print('запуск')
    app.run_polling()
