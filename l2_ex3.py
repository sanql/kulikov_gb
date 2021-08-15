# year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# u_mes = int(input('Введите номер месяца - '))
# if u_mes in year[0:3] or u_mes == 12:
#     season = 'Зима'
# elif u_mes in year[3:6]:
#     season = 'Весна'
# elif u_mes in year[6:9]:
#     season = 'Лето'
# elif u_mes in year[9:12]:
#     season = 'Осень'
#
# print(f'Сезон, к которому относится указанный месяц - {season}')

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Введите номер месяца - '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)