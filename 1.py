# Вычислить число pi c заданной точностью d 
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import factorial as fact
i = 1
sgn = -1
a = 13591409
b = 545140134
c = 640320
t = c ** (3/2)
s = a / t 
ss = 3
while str(ss)[:12] != '3.1415926535' :
    tmp = (sgn * fact(6*i) * (a + b*i) / 
    (fact(3*i) * fact(i) ** 3 * t * c**(3*i)))
    
    ss = 1 / (12*s)

k = int(input('Введите отрицательную степень числа d: '))
d = 10 ** k

if 0.0000000001 < d < 0.1:
    print(round(ss, -k))

