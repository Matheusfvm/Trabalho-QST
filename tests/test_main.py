from src.main import main

def test_main(monkeypatch, capsys):
    inputs = iter(["2023", "2", "28"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    assert "Reunião agendada para: 28 de Fevereiro de 2023" in captured.out