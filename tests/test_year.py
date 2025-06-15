from src.year import select_year, is_leap_year

def test_select_year(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2023")
    assert select_year() == 2023
    
    inputs = iter(["-1", "2023"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_year() == 2023

def test_is_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2020) == True
    assert is_leap_year(2021) == False