inventory = dict()
item = 0
weight = 0
max = 100
real = weight
info = 0
print('Ваш инвентарь пуст. Его необходимо заполнить')
while True :
    if real == 0 : print('Ваш инвентарь всё ещё пуст')
    else : print('Ваш инвентарь : {}. Его вес : {} кг'.format(inventory,real))
    info = input('Что вы хотите сделать с инвентарём? ')
    info = info.strip()
    info = info.capitalize()
    if (info == 'Добавить предмет') :
        if real < max :
            item = input('Какой предмет вы хотите добавить в инвентарь? ')
            item = item.strip()
            weight = input('Какой вес у добавленного предмета в килограммах? ')
            weight = weight.strip()
            if weight.isdigit() == True : weight = int(weight)
            else : print('Неизвестный вес предмета')
            if (real+weight > max) : print('Инвентарь переполнен')
            else :
                inventory[item] = weight
                real = real + weight
        else : print('Инвентарь переполнен')
    elif (info == 'Удалить предмет') :
        item = input('Какой предмет вы хотите удалить? ')
        item = item.strip()
        if (inventory.get(item) != None) :
            print('Вы удалили предмет из инвентаря : {}'.format(item))
            item = inventory.pop(item)
            real = real - item
            print('Текущий вес инвентаря : {} кг'.format(real))
        else : 
            print('У вас в инвентаре нет такого предмета')
            print('Ваш инвентарь : {}'.format(inventory))
    else : 
        print('Вы не можете выполнить данное действие')
        continue
    info = input('Если желаете продолжить работу с инвентарём, введите 1 ')
    if info == '1': continue
    else : break
print('Ваш инвентарь готов к использованию : {}. Его вес : {} кг'.format(inventory,real))