"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('salary.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    staff = []
    # my_list = my_file.read()
    my_list = my_file.read().split('\n')
    print(my_list)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           staff.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20тыс у {staff}, средний оклад {int(sum(map(int, salary)) / len(salary)/1000)}тыс.')