from unittest.mock import patch
import pytest
from src.year import select_year, is_leap_year

def test_select_year_valid_input():
    with patch('builtins.input', return_value='2023'):
        assert select_year() == 2023

def test_select_year_invalid_then_valid_input():
    with patch('builtins.input', side_effect=['-1', '2023']):
        assert select_year() == 2023

@pytest.mark.parametrize("year,expected", [
    (2000, True),    # Divisível por 400
    (1900, False),   # Divisível por 100 mas não por 400
    (2020, True),    # Divisível por 4 mas não por 100
    (2021, False),   # Não é bissexto
    (2400, True),    # Caso extremo
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected