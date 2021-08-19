# def my_func(x, y):
#     stepen = x ** y
#     return (f'{x} ** {y} = ', stepen)
#
# def main():
#     print(my_func(float(input('Num1 - ')), float(input('Num2 - '))))
#
# main()


def my_func(x, y):
    stepen = 1 / x
    while y < -1:
        y += 1
        stepen = stepen * 1 / x
    return f'{x} ** {y} = ', stepen

def main():
    print(my_func(float(input('Введите целое положительное число - ')), float(input('Введите целое отрицательное\\'
                                                                                    ' число - '))))

main()
