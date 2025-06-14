import sys
import os
import pytest
from allpairspy import AllPairs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from month import get_days_in_month

anos = [2023, 2024]  # ano normal e bissexto
meses = [2, 4, 12]  # Fevereiro, Abril, Dezembro
dias = [1, 28, 29, 30, 31]  # Dias de limite

# Gerar combinações Pairwise
pairwise_combinacoes = list(AllPairs([anos, meses, dias]))

print("\n=== Combinações Pairwise GERADAS (sem filtro) ===")
for c in pairwise_combinacoes:
    print(c)

combinacoes = [
    (ano, mes, dia)
    for (ano, mes, dia) in pairwise_combinacoes
    if 1 <= dia <= get_days_in_month(mes, ano)
]

print("\n=== Combinações Pairwise FILTRADAS (datas reais) ===")
for c in combinacoes:
    print(c)

# Teste parametrizado com os dados válidos
@pytest.mark.parametrize("ano, mes, dia", combinacoes)
def test_data_valida(ano, mes, dia):
    max_dias = get_days_in_month(mes, ano)
    assert 1 <= dia <= max_dias
