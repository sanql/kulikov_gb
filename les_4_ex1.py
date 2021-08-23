def zp_func():
    try:
        clocks = float(input('Выработка в часах - '))
        bet_clock = float(input('Ставка в час в рублях - '))
        bonus = float(input('Премия в рублях - '))
        zp = clocks * bet_clock + bonus
        print(f'заработная плата сотрудника - {zp}')
    except ValueError:
        return print('Некорректные данные!')
zp_func()