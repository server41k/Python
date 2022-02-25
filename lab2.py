# Подсчёт дня года и сезона
# С учётом високосных годов по григориансому календарю
# Created by Chaush Server
def main():
    day = get_day()
    month = get_month()
    year = get_year()
    year = visocosni(year)
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day > 31 or day < 1:
            print("Error date")
            exit()
    if month == 2 and year == 0:
        if day > 28 or day < 1:
            print("Error date")
            exit()
    if month == 2 and year == 1:
        if day > 29 or day < 1:
            print("Error date")
            exit()
    if month in (4, 6, 9, 11):
        if day > 30 or day < 1:
            print("Error date")
            exit()
    solution(day, month, year)


def visocosni(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0


def solution(day, month, year):
    if month == 1:
        year_day = day
    if month == 2:
        year_day = day+31
    if month == 3:
        year_day = day+31+28
    if month == 4:
        year_day = day+31+28+31
    if month == 5:
        year_day = day+31+28+31+30
    if month == 6:
        year_day = day+31+28+31+30+31
    if month == 7:
        year_day = day+31+28+31+30+31+30
    if month == 8:
        year_day = day+31+28+31+30+31+30+31
    if month == 9:
        year_day = day+31+28+31+30+31+30+31+31
    if month == 10:
        year_day = day+31+28+31+30+31+30+31+31+30
    if month == 11:
        year_day = day+31+28+31+30+31+30+31+31+30+31
    if month == 12:
        year_day = day+31+28+31+30+31+30+31+31+30+31+30
    if year == 1:
        if month > 2:
            year_day += 1
    print("------------------------------")
    print("День года: ", year_day)
    if month in (12, 1, 2):
        season = "Зима"
    if month in (3, 4, 5):
        season = "Весна"
    if month in (6, 7, 8):
        season = "Лето"
    if month in (9, 10, 11):
        season = "Осень"
    print("Сезон: ", season)
    if year == 1:
        print("Год високосный по грегорианскому календарю")
    else:
        print("Год невисокосный по грегорианскому календарю")
    print("------------------------------")


def get_day():
    while True:
        try:
            day = int(input("Введите день: "))
            break
        except:
            print("Может обойдёмся цифрами ?")
    return day


def get_month():
    while True:
        try:
            month = int(input("Введите месяц: "))
            break
        except:
            print("Может обойдёмся цифрами ?")
    if month < 1 or month > 12:
        print("Error date")
        exit()
    return month


def get_year():
    while True:
        try:
            year = int(input("Введите год: "))
            break
        except:
            print("Может обойдёмся цифрами ?")
    if year < 0:
        print("Error date")
        exit()
    return year


if __name__ == "__main__":
    main()
