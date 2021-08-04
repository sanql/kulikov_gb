dohod = int(input('Введите значение выручки фирмы - '))
rashod = int(input('Введите значение издержек фирмы - '))
if dohod > rashod:
    plus = dohod - rashod
    print('Прибыль фирмы = ', plus, 'ден. ед.')
    rent = plus / dohod * 100
    print('Прибыль фирмы = ', rent, '%')
    piople = int(input('Введите число сотрудников фирмы - '))
    print('Величина прибыли из рассчёта на одного сотрудника = ', plus / piople, 'ден. ед.')
elif dohod <= rashod:
    print('Предприятие работает в убыток. убыток составляет ', rashod - dohod, 'ден. ед.')
