import pytest
from allpairspy import AllPairs
from src.day import select_day, get_days_in_month

anos = [2023, 2024]
meses = list(range(1, 13))
dias = list(range(1, 32))

# Geração do modelo de parâmetros
parameters = [anos, meses, dias]


# Gerar combinações pairwise válidas
pairwise_ano_mes_dia = [
    (ano, mes, dia) for (ano, mes, dia) in AllPairs(parameters)
]

print("\n=== Casos de teste Ano-Mês-Dia (pairwise) ===")
for case in pairwise_ano_mes_dia:
    print(case)
print(len(pairwise_ano_mes_dia))

@pytest.mark.parametrize("ano, mes, dia", pairwise_ano_mes_dia)
def test_target_pairwise_ano_mes_dia(ano, mes, dia, monkeypatch, capsys):
    max_days = get_days_in_month(mes, ano)

    if 1 <= dia <= max_days:
        # Entrada válida: só um input necessário
        monkeypatch.setattr('builtins.input', lambda _: str(dia))
        resultado = select_day(mes, ano)
        assert resultado == dia
    else:
        # Entrada inválida seguida de válida para sair do loop
        inputs = iter([str(dia), '1'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        resultado = select_day(mes, ano)
        captured = capsys.readouterr()

        assert resultado == 1  # retorna o valor válido digitado depois do erro
        assert "Dia inválido. Tente novamente." in captured.out