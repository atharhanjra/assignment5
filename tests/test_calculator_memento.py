"""
Tests for the CalculatorMemento class (app/calculator_memento.py).

A memento is a saved snapshot of the calculator's history, used for undo and redo.
"""

from decimal import Decimal

import pytest

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


@pytest.mark.parametrize("operation, a, b", [
    ("Addition", "2", "3"),
    ("Multiplication", "4", "5"),
    ("Subtraction", "10", "4"),
])
def test_memento_round_trip(operation, a, b):
    """Saving a memento to a dictionary and loading it back gives the same history."""
    calc = Calculation(operation=operation, operand1=Decimal(a), operand2=Decimal(b))
    memento = CalculatorMemento(history=[calc])

    # Convert the memento to a dictionary, then back into a memento
    data = memento.to_dict()
    restored = CalculatorMemento.from_dict(data)

    assert restored.history[0].operation == calc.operation
    assert restored.history[0].result == calc.result
    assert restored.timestamp == memento.timestamp


def test_empty_memento():
    """A memento with no history still converts back and forth correctly."""
    memento = CalculatorMemento(history=[])
    restored = CalculatorMemento.from_dict(memento.to_dict())
    assert restored.history == []