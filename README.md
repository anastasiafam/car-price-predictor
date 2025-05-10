# README.md

# Car Price Predictor
ML-сервис для предсказания рыночной цены автомобиля на основе введённых характеристик.

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
│   └── api/
│       └── main.py        # FastAPI API
│   └── model/             # модель и параметры
├── data/
│   └── cars.csv           # датасет
├── tests/
│   └── test_api.py        # тесты API
├── streamlit_app.py       # визуальный интерфейс
├── train.py               # обучение модели
├── run_all.bat            # автозапуск API и UI
├── requirements.txt
└── README.md
```

---

## Авторы
МПИ-24-1-2, Фам Анастасия, Катызина Анастасия



