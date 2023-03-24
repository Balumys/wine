import datetime as dt


def get_year_suffix(year: int):
    if 11 <= year % 100 <= 14:
        return str("лет")
    if year % 10 in [2, 3, 4]:
        return str("года")
    if year % 10 == 1:
        return str("год")
    return str("лет")


def get_years_since_foundation_text():
    foundation_year = dt.date(year=1920, month=1, day=1).year
    delta = dt.datetime.now().year - foundation_year
    years_since_foundation_text = f"Уже {delta} {get_year_suffix(delta)} с Вами"
    return years_since_foundation_text
