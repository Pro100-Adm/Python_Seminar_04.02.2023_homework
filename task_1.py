def get_season_from_month_list(month_number):
    month_list = ["Зима", "Весна", "Лето", "Осень"]
    if month_number in ["1", "2", "12"]:
        return month_list[0]
    elif month_number in ["3", "4", "5"]:
        return month_list[1]
    elif month_number in ["6", "7", "8"]:
        return month_list[2]
    elif month_number in ["9", "10", "12"]:
        return month_list[3]
    else:
        return "Неверный номер месяца! "

def get_season_from_month_dict(month_number):
    month_dict = {"Зима": ('1', '2', '12'), "Весна": ('3', '4', '5'), "Лето": ('6', '7', '8'), "Осень": ('9','10','11')}
    return [k for (k, n) in month_dict.items() if month_number in n]


print(get_season_from_month_list(input("Введите номер месяца: ")))
print(*get_season_from_month_dict(input("Введите номер месяца: ")))