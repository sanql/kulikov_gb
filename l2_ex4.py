string = input('Введите строку - ')
list = string.split()
for i in range(len(list[:])):
    print(list[i][:10])


# Другое решение, без ограничения списка 10 символами...
# string = input('Введите строку - ')
# print('\n'.join(string.split()))