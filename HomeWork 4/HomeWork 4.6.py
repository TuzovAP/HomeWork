"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения
"""

from itertools import count
from itertools import cycle

counter = 0
for el in count(int(input('Введите стартовое число: '))):
    print(el)
    if el >= counter + 10:
        resume = input('Продолжим? (y - resume, q - exit) ').lower()
        if resume == 'q':
            print('Вы вышли из цикла')
            break
        counter += 10

print('\nВторое задание (повторение элементов)\n')
counter_list = 0
chek = 0
my_list = ['Привет', 'как', 'дела', 12]
for el in cycle(my_list):
    print(el, end=' ')
    if counter_list >= chek + 10:
        resume = input('\nПродолжим? (y - resume, q - exit) ').lower()
        if resume == 'q':
            print('Вы вышли из цикла')
            break
        else:
            chek += 10
    counter_list += 1
