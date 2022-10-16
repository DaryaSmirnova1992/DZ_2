# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input('Вещественное число: ')
a = a.replace('-', '')
a = a.replace('.', '')
a = a.replace(',', '')
b = list(a)

sum = 0
for i in b:
    sum += int(i)
    print(sum)
