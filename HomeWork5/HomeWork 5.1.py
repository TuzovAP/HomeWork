"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_f = open('test.txt', 'w')
line = input('Что запишем в файл? \n')
while line:
    my_f.writelines(line)
    line = input('Что еще добавим в файл? для выхода нажмите Enter \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()