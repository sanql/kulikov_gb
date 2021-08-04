#Перевод секунд в формат чч:мм:сс
time_sec = int(input('Введи количество секунд - '))
h = time_sec // 3600
if h < 10:
    h = '0' + str(h)
time_sec = time_sec % 3600
minute = time_sec // 60
if minute < 10:
    minute = '0' + str(minute)
sec = time_sec % 60
if sec < 10:
    sec = '0' + str(sec)
print(h,':',minute,':',sec)
