from src.day import select_day

def test_select_day(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "15")
    assert select_day(1, 2023) == 15
    
    inputs = iter(["0", "32", "20"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_day(1, 2023) == 20
    
    inputs = iter(["29"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_day(2, 2020) == 29