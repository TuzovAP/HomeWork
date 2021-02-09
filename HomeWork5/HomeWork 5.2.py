"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open('test2.txt', 'r', encoding='utf-8')
content = my_file.read()
print(f'Содержимое файла: \n {content}')

my_file.seek(0)
line_count = my_file.readlines()

my_file.seek(0)
word_count = my_file.read().split()

print(f'Количество строк в файле - {len(line_count)}')
print(f'Общее количество слов - {len(word_count)}')
my_file.close()
