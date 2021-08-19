def div_f(num_1: int, num_2: int) -> float: # Для других программистов, чтобы знали какие типы используются )))
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        return 'Ошибка "Деление на ноль"!'
    # except ValueError: (обработка ошибки не роисходит)
    #     return 'Некорректные данные!'
    return result

print(div_f(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
