import pytest
from allpairspy import AllPairs
from src.day import select_day, get_days_in_month

anos = [2023, 2024]  # ano normal e bissexto
meses = [2, 4, 12]  # Fevereiro, Abril, Dezembro
dias = [0, 1, 10, 13, 16, 24, 28, 29, 30, 31]  # Dias de limite

# Gerar combinações Pairwise
parameters = [anos, meses, dias]

casos_especiais = [
    # Ano bissexto: 29/02 válido
    (2024, 2, 29),

    # Ano não bissexto: 29/02 inválido
    (2023, 2, 29),

    # Limite inferior dia válido
    (2023, 1, 1),

    # Dia inválido menor que 1
    (2023, 1, 0),

    # Dia inválido maior que 31
    (2023, 1, 32),

    # Mês com 30 dias, dia 31 inválido
    (2023, 4, 31),

    # Mês com 30 dias, dia 30 válido
    (2023, 4, 30),

    # Mês com 31 dias, dia 31 válido
    (2023, 12, 31),

    # Dia 28 em fevereiro ano normal (válido)
    (2023, 2, 28),

    # Dia 30 em fevereiro (inválido)
    (2023, 2, 30),
]

combinacoes = [
    (ano, mes, dia) for (ano, mes, dia) in AllPairs(parameters)
]

for caso in casos_especiais:
    if caso not in combinacoes:
        combinacoes.append(caso)

print("\n=== Combinações Pairwise só com dias relevantes ===")
for c in combinacoes:
    print(c)
print(len(combinacoes))

# Teste parametrizado com os dados válidos
@pytest.mark.parametrize("ano, mes, dia", combinacoes)
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
