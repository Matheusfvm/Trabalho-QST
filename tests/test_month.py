from src.month import select_month, get_days_in_month

def test_select_month(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    month, name = select_month()
    assert month == 1
    assert name == "Janeiro"
    
    inputs = iter(["0", "13", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    month, name = select_month()
    assert month == 5

def test_get_days_in_month():
    assert get_days_in_month(1, 2023) == 31
    assert get_days_in_month(4, 2023) == 30
    assert get_days_in_month(2, 2023) == 28
    assert get_days_in_month(2, 2020) == 29