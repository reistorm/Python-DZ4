# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def find_simple_multipliers(list):
    list = []
    n = int(input('Введите число N: '))
    for i in range(1, 10):
        if n % i == 0:
            list.append(i)
        
    list.append(n)
    return list
print(find_simple_multipliers(list))