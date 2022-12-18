'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.'''

n = int(input('Введите число: '))
list = []
for i in range(-n, n +1):
    list.append(i)
for i in list:
    print(i, end=" ")

path = 'file.txt'
data = open(path, 'r')
proiz1 = list[int(data.readline())] * list[int(data.readline(2))]
proiz2 = list[int(data.readline(3))] * list[int(data.readline(4))]
print(f'\n{proiz1} \n{proiz2}')
