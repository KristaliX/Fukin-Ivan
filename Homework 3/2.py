z = 0
x = 0
y = 0
while z!='STOP' :
    print("Куда Вы хотите переместить персонажа?")
    z = input()
    c = z.split()
    if len(c) == 2 :
        if ((c[0] == 'Вправо') and (c[1].isdigit())) :
            q = int(c[1])
            x += q
        elif ((c[0] == 'Влево') and (c[1].isdigit())) :
            q = int(c[1])
            x -= q
        elif ((c[0] == 'Вверх') and (c[1].isdigit())) :
            q = int(c[1])
            y += q
        elif ((c[0] == 'Вниз') and (c[1].isdigit())) :
            q = int(c[1])
            y -= q
        else : print("Вы ввели недопустимое направление движения")    
    elif len(c) == 1 :
        if c[0] == 'Вправо' : x += 1
        elif c[0] == 'Влево' : x -= 1
        elif c[0] == 'Вверх' : y += 1
        elif c[0] == 'Вниз' : y -= 1
        elif z == 'STOP' :
            print("Вы ввели стоп-слово")
        else : print("Вы ввели недопустимое направление движения")
    else : print("Вы ввели недопустимое направление движения")
    print("Координаты Вашего персонажа : ({},{})".format(x,y))