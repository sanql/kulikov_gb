a = int(input('Значение в первый день (результат забега в км) - '))
b = int(input('Значение (в км), на которое необходимо равняться (цель) - '))
count = 1
while a < b:
    a = a + a / 10
    count += 1
print('День, на который будет достигнут результат - ', count)
