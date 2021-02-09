# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
# [1, 2, 3, 4, 5] => [2, 1, 4, 3, 5]

my_list = list(input('Введите даные: '))

item = 0
new_list = []
iteration = int(len(my_list) / 2)
i = 0

while i < iteration:
    new_list.append(my_list[item + 1])
    new_list.append(my_list[item])
    item += 2
    i += 1

if int(len(my_list) % 2) > 0:
    new_list.append(my_list[-1])

print(new_list)
