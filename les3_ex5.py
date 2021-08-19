def sum_str():
    summa = 0
    itogo = 0
    while True:
        str_num = input('Введите числа через пробел или q - для выхода ').split()
        for el in range(len(str_num)):
            if str_num[el] == 'q':
                break
            else:
                summa += int(str_num[el])
                print(f'Итоговая сумма = {itogo}')
        itogo += summa
    print(f'Итоговая сумма = {itogo}')

sum_str()