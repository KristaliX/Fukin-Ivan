import math
a = 0
b = 0
c = 0
D = 0
x1 = 0
x2 = 0
f = print('Введите коэффициенты квадратного уравнения (ax^2+bx+c=0)')
a = float(input('Введите a : '))
b = float(input('Введите b : '))
c = float(input('Введите c : '))
D = b**2-4*a*c
print('Дискриминант равен = {}'.format(D))
if D < 0 : print('Дискриминант отрицательный, корней нет')
elif D == 0 : 
    print('Дискриминант равен 0, один корень')
    x1 = (-b)/(2*a)
    print('Корень равен = {}'.format(x1))
else :
    print('Дискриминант больше нуля, два корня')
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print('Первый корень равен = {}'.format(x1))
    print('Второй корень равен = {}'.format(x2))