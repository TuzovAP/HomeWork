"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def summary():
    try:
        with open('file_5.txt', 'w+') as my_file:
            line = input('Введите цифры через пробел: \n')
            my_file.writelines(line)
            my_numb = line.split()

            print('Сумма введенных цифр: ', sum(map(int, my_numb)))

    except ValueError:
        print('Неправильно набран номер. Введите цифры')
summary()