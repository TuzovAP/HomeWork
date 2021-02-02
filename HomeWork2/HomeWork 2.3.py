# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

user_month = int(input('Введите номер месяца: '))

if user_month == 12 or user_month == 1 or user_month == 2:
    print(season_list[0])
    print(season_dict[1])
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(season_list[1])
    print(season_dict[2])
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(season_list[2])
    print(season_dict[3])
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(season_list[3])
    print(season_dict[4])
