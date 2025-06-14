from unittest.mock import patch, MagicMock
from src.main import main

def test_main_full_flow():
    # Configurando todos os mocks necessários
    with patch('src.main.select_year', return_value=2023) as mock_year, \
         patch('src.main.select_month', return_value=(2, "Fevereiro")) as mock_month, \
         patch('src.main.select_day', return_value=28) as mock_day, \
         patch('builtins.print') as mock_print:
        
        main()
        
        # Verificando se as funções foram chamadas corretamente
        mock_year.assert_called_once()
        mock_month.assert_called_once()
        mock_day.assert_called_once_with(2, 2023)
        
        # Verificando a saída final
        mock_print.assert_called_with("\nReunião agendada para: 28 de Fevereiro de 2023")