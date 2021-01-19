# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.


goods = []
user_goods = {'Название': '', 'Цена': '', 'Количество': '', 'Ед.измерения': ''}
goods_analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед.измерения': []}
number_goods = 0
feature_ = None
user_answer = None

while True:
    user_answer = input("Для добавления товара нажмите 'Enter' \nДля анализа нажмите 'A'\nДля выхода нажмите 'Q'").upper()
    if user_answer == 'Q' or user_answer == 'Й':
        break
    number_goods += 1
    if user_answer == 'A' or user_answer == 'Ф':
        for key, value in goods_analytics.items():
            print(f'{key}: {value}')
    for key_goods in user_goods.keys():
        feature_ = input(f'Введите "{key_goods}" товара: ')
        user_goods[key_goods] = int(feature_) if (key_goods == 'Цена' or key_goods == 'Количество') else feature_
        goods_analytics[key_goods].append(user_goods[key_goods])
    goods.append((number_goods, user_goods))
