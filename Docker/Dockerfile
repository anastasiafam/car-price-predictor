# Используем официальный slim-образ Python
FROM python:3.10-slim

WORKDIR /app

# Копируем файл зависимостей и устанавливаем зависимости
COPY ../requirements/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY ../ ./

# Устанавливаем supervisor для управления процессами
RUN apt-get update && apt-get install -y supervisor

COPY ./Docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf


# Открываем порты для FastAPI и Streamlit
EXPOSE 8000 
EXPOSE 8501 

# Запускаем supervisord для запуска двух процессов
CMD ["/usr/bin/supervisord"]