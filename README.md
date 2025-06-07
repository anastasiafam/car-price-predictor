# README.md

# Car Price Predictor
ML-сервис для предсказания рыночной цены автомобиля на основе введённых характеристик.

## 📝 Мотивация

Этот проект разработан для демонстрации полного цикла создания машинного обучения сервиса:
- Обучение модели на реальных данных
- Сохранение модели для дальнейшего использования
- Создание REST API для предсказаний с помощью FastAPI
- Разработка простого пользовательского интерфейса с использованием Streamlit
- Написание автоматических тестов для API и модели
- Настройка CI/CD для автоматизации проверки качества кода
- Подготовка проекта к развертыванию в продакшн среду с использованием Docker


## Стек технологий
- Python 3.8+
- CatBoost — модель машинного обучения
- FastAPI — создание REST API
- Streamlit — создание пользовательского интерфейса
- Optuna — оптимизация гиперпараметров
- Pydantic — валидация данных
- Pytest — тестирование
- Docker, Docker Compose — контейнеризация
- GitHub Actions — CI/CD

## Установка и запуск

1. **Клонируй репозиторий и перейди в директорию проекта:**
   ```bash
   git clone https://github.com/anastasiafam/car-price-predictor.git
   cd car-price-predictor
   ```

2. **Создай виртуальное окружение и активируй:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Установи зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Обучи модель и сохрани её:**
   ```bash
   python app/pipeline.py
   ```

5. **Запусти проект через Docker Compose:**
   ```bash
   docker-compose up --build
   ```
   После запуска:
- FastAPI API будет доступен на: [http://localhost:8000/docs](http://localhost:8000/docs)
- Streamlit интерфейс будет доступен на: [http://localhost:8501](http://localhost:8501)

## Тесты API
Запусти тесты API с помощью:
```bash
pytest tests/test_api.py
```

## Тесты tox
Запусти тесты tox с помощью:
```bash
tox
```

## Структура проекта
```
car-price-predictor/
├── app/                   # Основная папка с приложением
│   ├── api/              
│   │   └── main.py        # Основная логика API для предсказаний
│   ├── data/            
│   │   └── cars.csv       # Датасет с данными о машинах
│   ├── logs
│   │   └── car.log        # Лог-файл
│   ├── model/             # Модели
│   │   ├── model.pkl      # Обученная модель
│   │   └── results.json   # Результаты работы модели
│   ├── config.yaml        # Конфигурационный файл
│   ├── logger.py          # Настройки логирования
│   ├── pipeline.py        # Логика обработки данных и обучения данных
│   └── streamlit_app.py   # Интерфейс для приложения на Streamlit
├── Docker/
│   ├── Dockerfile         # Dockerfile
│   └── supervisord.conf   # Конфигурация supervisord
├── requirements/          # Папка с зависимостями проекта
│   ├── dev_requirements.txt  # Зависимости для typechecks, stylechecks, lint
│   ├── requirements.txt      # Основные зависимости
│   └── test_requirements.txt # Зависимости для тестов
├── tests/                
│   └── test_api.py        # Тесты для API
├── LICENSE                
├── README.md              
├── tox.ini                # Конфигурация для tox
├── mypy.ini               # Конфигурация для mypy (проверка типов)
├── docker-compose.yml     # Docker-compose сборка
└── pyproject.toml         # Конфигурация системы сборки проекта       
```

---

## 👩‍💻 Авторы

Студенты группы МПИ-24-1-2:
- Фам Анастасия — [m2004149@edu.misis.ru](mailto:m2004149@edu.misis.ru)
- Катызина Анастасия — [m2000743@edu.misis.ru](mailto:m2000743@edu.misis.ru)

Проект создан в рамках учебной работы в НИТУ МИСиС, 2025.



