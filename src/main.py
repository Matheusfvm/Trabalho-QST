from src.year import select_year  # Modificado
from src.month import select_month  # Modificado
from src.day import select_day  # Modificado

def main():
    print("\n----- Agendar uma reunião ----- ")
    print("\nSelecione a data que deseja marcar: ")

    year = select_year()
    month, month_name = select_month()
    day = select_day(month, year)

    print(f"\nReunião agendada para: {day} de {month_name} de {year}")

if __name__ == "__main__":
    main()