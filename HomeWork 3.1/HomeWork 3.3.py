# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def max_two_arg(arg, arg2, arg3):
    new_list = (arg, arg2, arg3)
    new_list = sorted(new_list)
    summ_max_arg = new_list[-2] + new_list[-1]
    print(summ_max_arg)

max_two_arg(1, 2, 3)