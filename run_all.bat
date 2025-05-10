@echo off
REM Открываем сервер FastAPI
start powershell -NoExit -Command "cd car-price-predictor; uvicorn app.api.main:app --reload"

REM Ждем пару секунд, чтобы uvicorn успел запуститься
timeout /t 3 > nul

REM Открываем Streamlit
start powershell -NoExit -Command "cd car-price-predictor; streamlit run streamlit_app.py"
