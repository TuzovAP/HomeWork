"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)

Пример словаря:
{“Информатика”: 170, “Физика”: 40}

"""
# def integer(object):
#     digit = []
#     a = 0
#     while a <= len(object):
#         if object[a].isdigit():
#             digit.append(object[a])
#             a +=1
#     print(digit)


subj = {}
with open('file_6.txt', 'r', encoding='utf-8') as init_f:
    lecture_all =[]
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        lecture = lecture.replace("(л)", "")
        practice = practice.replace("(пр)", "")
        lab = lab.replace("(лаб)", "")

        subj[subject] = int(lecture) + int(practice) + int(lab)
    # print(f'Общее количество часов по предмету - \n {subj}')