def live_bytes (x) :
    for i in range (len(x)) : x[i] = x[i].encode('utf-8')
    print('Список байт кодов вашего списка строк : {}'.format(x))
    return

def dead_bytes (x) :
    for i in range (len(x)) : x[i] = x[i].decode('utf-8')
    print('Преобразование списка байт кодов в список строк : {}'.format(x))
    return

a = list()
b = 0
while True :
    b = (input('Введите вашу строку : '))
    if b == 'STOP' : break
    else : a.append(b)
print('Вы ввели следующий список строк : {}'.format(a))
live_bytes(a)
dead_bytes(a)