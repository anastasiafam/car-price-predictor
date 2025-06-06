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
   python train.py
   ```

5. **Запусти проект через Docker Compose:**
   ```bash
   docker-compose up --build
   ```
   После запуска:
- FastAPI API будет доступен на: [http://localhost:8000/docs](http://localhost:8000/docs)
- Streamlit интерфейс будет доступен на: [http://localhost:8501](http://localhost:8501)

## Тесты
Запусти тесты API с помощью:
```bash
pytest tests/test_api.py
```

## Структура проекта
```
car-price-predictor/
├── app/
│ ├── api/
│ │ └── main.py    # FastAPI API для предсказаний
│ └── model/       # сохраненная модель
├── data/
│ └── cars.csv     # обучающий датасет
├── tests/
│ └── test_api.py  # тесты API
├── streamlit_app.py 
├── train.py       # обучение модели CatBoost
├── run_all.bat    # автоматический запуск API и Streamlit
├── requirements.txt 
├── pyproject.toml # настройки сборки пакета
├── LICENSE 
└── README.md 
```

---

## 👩‍💻 Авторы

Студенты группы МПИ-24-1-2:
- Фам Анастасия — [m2004149@edu.misis.ru](mailto:m2004149@edu.misis.ru)
- Катызина Анастасия — [m2000743@edu.misis.ru](mailto:m2000743@edu.misis.ru)

Проект создан в рамках учебной работы в НИТУ МИСиС, 2025.



