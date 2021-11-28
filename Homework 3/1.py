x = 0
y = 0
print("Куда Вы хотите переместить персонажа?")
z = input()
z = z.split()
if len(z) == 2 :
    if ((z[0] == 'Вправо') and (z[1].isdigit())) :
         q = int(z[1])
         x += q
    elif ((z[0] == 'Влево') and (z[1].isdigit())) :
         q = int(z[1])
         x -= q
    elif ((z[0] == 'Вверх') and (z[1].isdigit())) :
         q = int(z[1])
         y += q
    elif ((z[0] == 'Вниз') and (z[1].isdigit())) :
         q = int(z[1])
         y -= q
    else : print("Вы ввели недопустимое направление движения")    
elif len(z) == 1 :
    if z[0] == 'Вправо' : x += 1
    elif z[0] == 'Влево' : x -= 1
    elif z[0] == 'Вверх' : y += 1
    elif z[0] == 'Вниз' : y -= 1
    else : print("Вы ввели недопустимое направление движения")
else : print("Вы ввели недопустимое направление движения")
print("Координаты Вашего персонажа : ({},{})".format(x,y))