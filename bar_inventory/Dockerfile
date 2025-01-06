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

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код приложения
COPY . .

# Устанавливаем переменную окружения для работы с FastAPI
ENV PYTHONUNBUFFERED=1

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
















# # Используем Python 3.10 на основе более стабильного Debian Bullseye
# FROM python:3.10-slim-bullseye

# # Устанавливаем рабочую директорию
# WORKDIR /app

# # Устанавливаем системные зависимости с обновлением ключей
# RUN apt-get update && apt-get install -y \
#     gnupg curl && \
#     curl -fsSL https://ftp-master.debian.org/keys/archive-key-12.asc | gpg --dearmor -o /usr/share/keyrings/debian-archive-keyring.gpg && \
#     curl -fsSL https://ftp-master.debian.org/keys/archive-key-13.asc | gpg --dearmor -o /usr/share/keyrings/debian-security-archive-keyring.gpg && \
#     apt-get update && \
#     apt-get install -y --no-install-recommends \
#     build-essential \
#     libpq-dev \
#     libssl-dev \
#     libffi-dev \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# # Копируем файл зависимостей
# COPY requirements.txt .

# # Устанавливаем Python-зависимости
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt

# # Копируем приложение
# COPY . .

# # Открываем порт
# EXPOSE 8000

# # Запускаем приложение
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000"]
























# # Используем официальный образ Python
# FROM python:3.10-slim-bullseye

# # Устанавливаем необходимые зависимости
# RUN apt-get update && apt-get install -y \
#     apt-utils \
#     gnupg \
#     curl \
#     build-essential \
#     libpq-dev \
#     libssl-dev \
#     libffi-dev && \
#     curl -fsSL https://ftp-master.debian.org/keys/archive-key-12.asc | gpg --dearmor -o /usr/share/keyrings/debian-archive-keyring.gpg && \
#     curl -fsSL https://ftp-master.debian.org/keys/archive-key-13.asc | gpg --dearmor -o /usr/share/keyrings/debian-security-archive-keyring.gpg && \
#     apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*

# # Создаём и устанавливаем рабочую директорию
# WORKDIR /app

# # Копируем файл зависимостей и устанавливаем их
# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем остальной код приложения
# COPY . .

# # Устанавливаем переменную окружения для работы с FastAPI
# ENV PYTHONUNBUFFERED=1

# # Открываем порт, на котором будет работать приложение
# EXPOSE 8000

# # Команда для запуска приложения
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
