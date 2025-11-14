# Напишите функцию , которая принимает один аргумент — номер месяца
# — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

num_month = int(input('Введите номер месяца:   '))
def month_to_season(num_month):
    if num_month >= 3 and num_month <= 5:
        return 'Весна'
    elif num_month > 5 and num_month <= 8:
        return 'Лето'
    elif num_month > 8 and num_month <= 11:
        return 'Осень'
    elif num_month == 12 or num_month == 1 or num_month == 2:
        return 'Зима'
    else:
        return 'Укажите целое число от 1 до 12'
print(month_to_season(num_month))