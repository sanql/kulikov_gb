new_list = []
while True:
    change = input('Для продолжения ввода нажмите ENTER, для выхода - q - ')
    if change == 'q':
        break
    new_list.append(input('Введите элемент списка - '))

i = 0
while i <= len(new_list) // 2:
    temp = new_list[i]
    new_list[i] = new_list[i + 1]
    new_list[i + 1] = temp
    i += 2

print(f'Новая последовательность - {new_list}')
