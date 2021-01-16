# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input( "Введите время в секундах: " ))

time_hours = int(user_time / 60 / 60)
time_minutes = int((user_time / 60) - 60)
time_seconds = user_time % 60
print('Получается {hour}ч:{minutes}мин:{seconds}сек'.format(
    hour=time_hours,
    minutes=time_minutes,
    seconds=time_seconds,
))