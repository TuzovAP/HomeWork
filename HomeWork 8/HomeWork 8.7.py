"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z_summ = a + b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z ({self.z_summ + other.a + other.b}) = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a} + {self.b * other.b}'

    def __str__(self):
        return f'z ({self.z_summ}) = {self.a} + {self.b}'


z_1 = ComplexNumber(1, 2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)