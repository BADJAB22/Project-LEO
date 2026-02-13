#!/bin/bash

echo "--- Project LEO Installation Script ---"
echo "By Kadropic Labs / Bader Jamal"

# Check for Python
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python 3.9 or higher."
    exit
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    # Default dependencies if requirements.txt is missing
    pip install requests openai python-dotenv
fi

# Create data directory if it doesn't exist
mkdir -p data

echo "--- Installation Complete ---"
echo "To start Project LEO, run:"
echo "source venv/bin/activate && python3 main.py"
