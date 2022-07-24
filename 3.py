# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

def fib(n):
    
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Введите число: "))
numbers = []
for e in range(1, n):
    numbers.append(fib(e))
print(numbers)

def get_unique_numbers(numbers):
    list = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
            list.append(number)
    return list
print(get_unique_numbers(numbers))