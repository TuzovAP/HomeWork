"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1; Two — 2; Three — 3; Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл
"""

translat = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r', encoding='utf-8') as my_file:
    print(f'Исходный файл: {my_file.readlines()}')
    my_file.seek(0)
    for i in my_file:
        i = i.split()
        new_file.append(translat[i[0]] + ' — ' + i[2])



with open('file_4_new.txt', 'w+', encoding='utf-8') as my_file_new:
    my_file_new.write('\n'.join(new_file))
    my_file_new.seek(0)
    print(f'Новый файл: {my_file_new.readlines()}')

