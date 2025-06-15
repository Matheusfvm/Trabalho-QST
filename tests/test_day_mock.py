from unittest.mock import patch
import pytest
from src.day import select_day

def test_select_day_valid_input():
    with patch('builtins.input', return_value='15'):
        assert select_day(1, 2023) == 15  # Janeiro

def test_select_day_invalid_then_valid_input():
    with patch('builtins.input', side_effect=['0', '32', '20']):
        assert select_day(1, 2023) == 20

def test_select_day_february_leap():
    with patch('builtins.input', return_value='29'):
        assert select_day(2, 2020) == 29  # Fevereiro bissexto

def test_select_day_february_non_leap():
    with patch('builtins.input', side_effect=['29', '28']):
        assert select_day(2, 2023) == 28  # Fevereiro não bissexto