@echo off

chcp 65001 >nul

echo ✏️ Starting installation...

REM Check if Python 3.10.11 is available
py -3.10 --version > version.txt 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python 3.10.11 is not installed or not found. Please install Python 3.10.11 and try again.
    echo You can download Python 3.10.11 from: https://www.python.org/downloads/release/python-31011/
    exit /b 1
)

REM Read the Python version
set /p python_version=<version.txt
del version.txt

echo Detected Python version: %python_version%

REM Verify the version is exactly 3.10.11
echo %python_version% | find "3.10.11" >nul
if %errorlevel% neq 0 (
    echo ❌ Python 3.10.11 is required. Detected version: %python_version%.
    echo You can download Python 3.10.11 from: https://www.python.org/downloads/release/python-31011/
    exit /b 2
)

echo ✅ Python 3.10.11 is available.

REM Git clone the required repository
if not exist "Music-Source-Separation-Training\" (
    REM Check if Git is available
    git --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Git is not installed or not in PATH. Please install Git and try again.
        exit /b 3
    )
    echo ✅ Git is available.

    echo ⏳ Cloning git repository https://github.com/jarredou/Music-Source-Separation-Training [branch: colab-inference]
    git clone -b colab-inference https://github.com/jarredou/Music-Source-Separation-Training
    echo ✅ Cloned repository.
) else (
    echo ✅ Repository folder `Music-Source-Separation-Training` already exists.
)

REM Check if the .venv folder exists
if not exist ".venv\" (
    echo 🔍 .venv folder not found. Creating virtual environment...
    py -3.10 -m venv .venv --upgrade-deps
    if not exist ".venv\Scripts\python.exe" (
        echo ❌ Failed to create the virtual environment.
        exit /b 4
    )
    echo ✅ Created virtual environment .venv.
) else (
    echo ✅ .venv folder already exists.
)

REM Install pip requirements
echo ⏳ Installing dependencies... This will take a few minutes.
.\.venv\Scripts\python.exe -m pip install -r ".\requirements.txt"
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies.
    exit /b 5
)
echo ✅ Installed dependencies.

REM Create the necessary folders and ignore errors if they already exist
mkdir "input" "output" 2>nul
echo ✅ Created directories: input, output
echo ✅ Installation complete.