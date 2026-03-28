# Используем официальный Python 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Экспортируем переменные окружения (Docker не умеет читать .env напрямую)
# Но можно потом передавать при запуске контейнера через --env-file .env
# ENV TELEGRAM_BOT_TOKEN=тут_токен

# Запуск бота
CMD ["python", "main.py"]