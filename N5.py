Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
'''

from functools import reduce

list = [i for i in range(100, 1001) if i % 2 == 0]
multiplication = reduce((lambda a, b: a * b), list)
print(multiplication)