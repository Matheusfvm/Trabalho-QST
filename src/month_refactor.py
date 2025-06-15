MONTHS = {
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

def display_months():
    print("\nAvailable months:")
    for idx, (name, _) in MONTHS.items():
        print(f"{idx} - {name}")

def validate_month(value):
    try:
        month = int(value)
        if 1 <= month <= 12:
            return month
    except ValueError:
        pass
    return None

def get_valid_month():
    while True:
        user_input = input("Select a month (1-12): ")
        month = validate_month(user_input)
        if month:
            return month
        print("\nInvalid month. Please try again.")

def select_month():
    display_months()
    month = get_valid_month()
    name, _ = MONTHS[month]
    return month, name
