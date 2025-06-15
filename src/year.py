def select_year():
    while True:
        try:
            year = int(input("\nDigite um ano: "))
            if year < 0:
                raise ValueError
            return year
        
        except ValueError:
            print("Ano inválido. Tente novamente.")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
