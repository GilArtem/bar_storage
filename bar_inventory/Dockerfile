
# Используем официальный образ Python
FROM python:3.10-slim-bullseye

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    apt-utils \
    gnupg \
    curl \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Создаём и устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и создаём виртуальную среду
COPY requirements.txt .

# Создаём виртуальную среду
RUN python -m venv /venv

# Активируем виртуальную среду и устанавливаем зависимости
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Копируем остальной код приложения
COPY . .

# Устанавливаем переменную окружения для работы с FastAPI
ENV PYTHONUNBUFFERED=1

# Устанавливаем переменную окружения для использования виртуальной среды
ENV PATH="/venv/bin:$PATH"

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
