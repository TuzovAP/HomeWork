# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

def user_data(name, surname, birth_year, sity, email, phone):
    print(f'Имя: {name}, Фимилия: {surname}, Год рождения: {birth_year},', end=' ')
    print(f'Город проживания: {sity}, Email: {email}, Телефон: {phone}')

name = 'Иван'
surname = 'Иванов'
birth_year = 1987
sity = 'СПб'
email = 'spb@mail.tu'
phone = '+7-123-45-67-89'

user_data(name, surname, birth_year, sity, email, phone)