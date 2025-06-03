# README.md

# Car Price Predictor
ML-сервис для предсказания рыночной цены автомобиля на основе введённых характеристик.

## 📝 Мотивация

Этот проект разработан для демонстрации полного цикла создания машинного обучения сервиса:
- Обучение модели на реальных данных,
- Сохранение модели для дальнейшего использования,
- Создание REST API для предсказаний с помощью FastAPI,
- Создание простого пользовательского интерфейса с использованием Streamlit,
- Написание тестов для API,
- Подготовка проекта к развертыванию и эксплуатации.


## Стек технологий
- Python
- CatBoost
- FastAPI
- Streamlit
- Optuna
- pytest

## Установка и запуск

1. **Клонируй проект и перейди в папку:**
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

5. **Запусти проект автоматически:**
   ```bash
   run_all.bat
   ```
   Этот файл откроет 2 окна:
   - один терминал с FastAPI (http://localhost:8000/docs)
   - второй — со Streamlit интерфейсом (http://localhost:8501)

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



