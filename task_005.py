'''Реализуйте алгоритм перемешивания списка.'''
import random

num = int(input('Задайте размер списка: '))
list = []
for i in range(num):
    list.append(random.randint(0, 9))
print(list)

a = ''

while a != 'exit':
    for i in range(10):
        rand_1 = random.randint(0, num-1)
        rand_2 = random.randint(0, num-1)
        temp = list[rand_1]
        list[rand_1] = list[rand_2]
        list[rand_2] = temp
    print(list)
    a = input('Для повторного перемешивания списка нажмите Enter, для выхода введите exit: ')