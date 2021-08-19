def my_func(num1, num2, num3):
    numbs = [num1, num2, num3]
    numbs.remove(min(num1, num2, num3))
    return 'Сумма наибольших чисел = ', sum(numbs)

def main():
    print(my_func(int(input('Num1 - ')), int(input('Num2 - ')), int(input('Num3 - '))))

main()

# def my_func(num1, num2, num3):
#     numbs = [num1, num2, num3]
#     numbs.remove(min(num1, num2, num3))
#     return sum(numbs)
#
# def main():
#     print('Сумма наибольших чисел = ', my_func(8, 4, 9))
#
# main()
