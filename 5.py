# Даны два файла, в каждом из которых находится
# запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

with open('file1.txt', 'w') as file:
    file.write('x ** 2 + 1\n')
    

with open('file2.txt', 'w') as file:
    file.write('2*x - 3\n')
    

