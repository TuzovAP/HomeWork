# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_integer_number = int(input("Введите целое число:" ))

max_number = 0

while user_integer_number > 10:
    last_number = user_integer_number % 10
    user_integer_number = user_integer_number // 10
    if last_number > max_number:
        max_number = last_number

print(max_number)
