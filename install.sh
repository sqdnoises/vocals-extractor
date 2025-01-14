#!/usr/bin/env bash

# Exit on error
set -e

# Ensure the script is running with UTF-8 locale
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Check if Python 3.10 is available
echo "✏️ Starting installation..."
if ! command -v python3.10 >/dev/null 2>&1; then
    echo "❌ Python 3.10 is not installed or not found. Please install Python 3.10 and try again."
    echo "You can download Python 3.10 from: https://www.python.org/downloads/"
    exit 1
fi

# Read Python version
PYTHON_VERSION=$(python3.10 --version 2>&1 | awk '{print $2}')
echo "🔍 Detected Python version: $PYTHON_VERSION"

# Verify the version starts with 3.10
if [[ ! "$PYTHON_VERSION" =~ ^3\.10\. ]]; then
    echo "❌ Python 3.10.x is required. Detected version: $PYTHON_VERSION."
    echo "You can download Python 3.10 from: https://www.python.org/downloads/"
    exit 2
fi

echo "✅ Python 3.10 is available."

# Git clone the required repository
if [[ ! -d "Music-Source-Separation-Training" ]]; then
    if ! command -v git >/dev/null 2>&1; then
        echo "❌ Git is not installed or not in PATH. Please install Git and try again."
        exit 3
    fi

    echo "✅ Git is available."

    echo "⏳ Cloning git repository https://github.com/jarredou/Music-Source-Separation-Training [branch: colab-inference]"
    git clone -b colab-inference https://github.com/jarredou/Music-Source-Separation-Training
    echo "✅ Cloned repository."
else
    echo "✅ Repository folder 'Music-Source-Separation-Training' already exists."
fi

# Check if the .venv folder exists and create if needed
if [[ ! -d ".venv" ]]; then
    echo "🔍 .venv folder not found. Creating virtual environment..."
    python3.10 -m venv .venv --upgrade-deps
    if [[ ! -f ".venv/bin/python3" ]]; then
        echo "❌ Failed to create the virtual environment."
        exit 4
    fi
    echo "✅ Created virtual environment .venv."
else
    echo "✅ .venv folder already exists."
fi

# Source the virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

if [[ ! "$VIRTUAL_ENV" ]]; then
    echo "❌ Failed to activate virtual environment."
    exit 5
fi

echo "✅ Virtual environment activated."

# Install pip requirements
echo "⏳ Installing dependencies... This will take a few minutes."
python3 -m pip install -r "requirements.txt"
if [[ $? -ne 0 ]]; then
    echo "❌ Failed to install dependencies."
    deactivate
    exit 6
fi
echo "✅ Installed dependencies."

# Create the necessary folders
mkdir -p "input" "output"
echo "✅ Created directories: input, output"

# Deactivate the virtual environment
deactivate
echo "✅ Installation complete."