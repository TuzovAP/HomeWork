# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


result_list = [2, 'text', 456, 45.3, None]

def type_checking (list_elements):
    for element in list_elements:
        print(type(element))

type_checking(result_list)
