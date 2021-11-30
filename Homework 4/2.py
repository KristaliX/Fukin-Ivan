a = dict()
x = 0
key = 0
value = 0
while True:
    key = input('Введите ключ (название или кодировка цвета) : ')
    key = key.strip()
    value = (input('Введите значение (rgb) : '))
    value = value.strip()
    value = value.split()
    a[key] = tuple(value)
    print('Ваш словарь цветов : {}'.format(a))
    x = input('Желаете продолжить?(Да или нет) : ')
    if x == 'Нет' : break
    elif x == 'Да' : continue
    else :
        print('Неизвестный ответ')
        break
print('Ваш словарь цветов готов. {}'.format(a))
x = input('Введите название или кодировку цвета, чтобы узнать его rgb-значение : ')
x = x.strip()
print('Данные по Вашему запросу : {}'.format(a.get(x)))