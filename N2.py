Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''

list = [123, 201, -56, 320, 125, 3654, 874, 145, 658]

new_list = [list[i] for i in range(len(list)) if list[i] > list[i - 1]]
print(f'Исходный список: {list}')
print(f'Преобразованный список: {new_list}')