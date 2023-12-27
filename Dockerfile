# Используйте официальный образ Python
FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию в /app
WORKDIR /app

# Копируйте текущий каталог в рабочую директорию внутри контейнера
COPY . /app

# Установите зависимости, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Экспортируйте порт, который будет слушать ваше приложение Django
EXPOSE 8000

# CMD команда для запуска приложения (обратите внимание, что здесь указан IP 0.0.0.0)
CMD ["python", "main_app/manage.py", "runserver", "0.0.0.0:8000"]
