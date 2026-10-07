# Enhanced Calculator

A command-line calculator I built in Python for Module 5. It saves your calculation history to a CSV file and lets you undo and redo.

## Features

- Operations: add, subtract, multiply, divide, power, root
- Commands: help, history, clear, undo, redo, save, load, exit
- History is saved to a CSV file using pandas
- Settings are loaded from a `.env` file using python-dotenv
- 100% test coverage, checked by GitHub Actions

## Design Patterns

- **Factory:** creates the right operation from what you type
- **Strategy:** each operation is its own class
- **Observer:** logs and auto-saves each calculation
- **Memento:** saves history snapshots for undo and redo
- **Facade:** the `Calculator` class connects everything in one place

## Setup

```
git clone https://github.com/atharhanjra/assignment5.git
cd assignment5
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Settings (optional)

You can create a `.env` file to change settings, for example:

```
CALCULATOR_MAX_HISTORY_SIZE=1000
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
```

If you skip this, the calculator uses default settings.

## Usage

Start the calculator:

```
python3 main.py
```

Type an operation, then enter two numbers:

```
Enter command: add
First number: 2
Second number: 3

Result: 5
```

Type `help` to see all commands, or `exit` to quit.

## Running Tests

```
pytest --cov=app --cov-report=term-missing
```

## GitHub Actions

Tests run automatically on every push. The build fails if any test fails or coverage drops below 100%.