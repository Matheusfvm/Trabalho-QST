from unittest.mock import patch
import pytest
from src.month import select_month, get_days_in_month

def test_select_month_valid_input():
    with patch('builtins.input', return_value='1'):
        month, name = select_month()
        assert month == 1
        assert name == "Janeiro"

def test_select_month_invalid_then_valid_input():
    with patch('builtins.input', side_effect=['0', '13', '5']):
        month, name = select_month()
        assert month == 5

@pytest.mark.parametrize("month,year,expected", [
    (1, 2023, 31),   # Janeiro
    (4, 2023, 30),   # Abril
    (2, 2023, 28),   # Fevereiro não bissexto
    (2, 2020, 29),   # Fevereiro bissexto
    (7, 2023, 31),   # Julho
    (9, 2023, 30),   # Setembro
])
def test_get_days_in_month(month, year, expected):
    assert get_days_in_month(month, year) == expected