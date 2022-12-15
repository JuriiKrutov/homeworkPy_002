'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.'''
num = int(input('Введите число: '))
list = []
p = 1
for i in range(1, num+1):
    p = 1
    for j in range(1, i+1):        
        p *= j
    list.append(p)
print(list)
