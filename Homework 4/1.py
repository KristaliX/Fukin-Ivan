import random
a = list()
b = 0
N = 10
for i in range (N) : a.append(random.randint(1,99))
print('Список чисел : {}'.format(a))
for i in range (N-1) :
    for j in range (N-i-1) :
        if a[j] > a [j+1] :
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b
print('Отсортированный список : {}'.format(a))