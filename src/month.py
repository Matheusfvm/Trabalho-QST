from src.year import is_leap_year

MONTHS = {
    1: ("Janeiro", 31),
    2: ("Fevereiro", 28),
    3: ("Março", 31),
    4: ("Abril", 30),
    5: ("Maio", 31),
    6: ("Junho", 30),
    7: ("Julho", 31),
    8: ("Agosto", 31),
    9: ("Setembro", 30),
    10: ("Outubro", 31),
    11: ("Novembro", 30),
    12: ("Dezembro", 31)
}

def select_month():
    print("\nMeses disponíveis:")
    for idx, (name, _) in MONTHS.items():
        print(f"{idx} - {name}")

    while True:
        try:
            month = int(input("Selecione um mês (1-12): "))
            if month < 1 or month > 12:
                raise ValueError
            
            month_name, _ = MONTHS[month]
            return month, month_name
        
        except ValueError:
            print("\nMês inválido. Tente novamente.")

def get_days_in_month(month, year):
    days = MONTHS[month][1]

    if month == 2 and is_leap_year(year):
        return 29
    return days