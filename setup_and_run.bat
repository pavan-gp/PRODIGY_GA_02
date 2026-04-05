@echo off
echo ===========================================
echo       Setting up Text-to-Image Generator
echo ===========================================

IF NOT EXIST venv (
    echo [1/3] Creating virtual environment...
    python -m venv venv
) ELSE (
    echo [1/3] Virtual environment already exists.
)

echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/3] Installing dependencies...
echo Note: Downloading PyTorch may take a few minutes as it is quite large!
pip install -r requirements.txt

echo.
echo Setup Complete! Starting the application...
echo.

python app.py

pause
