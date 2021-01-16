# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км. (3.22)

# start = int(input("Начальный результат км:" ))
# target = int(input("Цель:" ))
start = 2
target = 3
day = 1
while target > start:
    start = start * 1.1
    day += 1
print(f'на {day}-й день спортсмен достиг результата — не менее {target} км.')

