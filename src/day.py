from src.month import get_days_in_month

def select_day(month, year):
    max_days = get_days_in_month(month, year)

    while True:
        try:
            day = int(input(f"\nSelecione um dia (1-{max_days}): "))
            if day < 1 or day > max_days:
                raise ValueError
            return day
        
        except ValueError:
            print("Dia inválido. Tente novamente.")