import random

a = set()
b = set()
N = 10

for i in range(N): 
    a.add(random.randint(1, 99))
    b.add(random.randint(1, 99))

print('Первое множество : {}'.format(a))
print('Второе множество : {}'.format(b))
print('Элементы, которые входят в оба множества : {}'
                          .format(a.intersection(b)))
print('Элементы, которые входят только в первое множество : {}'
                                      .format(a.difference(b)))
print('Элементы, которые входят только во второе множество : {}'
                                       .format(b.difference(a)))
print('Элементы, которые в первое или второе, но не входят в оба : {}'
                                   .format(a.symmetric_difference(b)))