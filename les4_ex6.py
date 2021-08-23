from itertools import count, cycle



print('Программа генерирует целвые числа, начиная с указанного. Для генерации следующего числа необходимо нажать Enter',
      ' для выхода нажмите q')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода',
      ' из программы нажмите q')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter_ = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()
