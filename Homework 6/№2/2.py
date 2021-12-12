C = 0
H = 0
O = 0
molecule = 0

try:
    with open('Homework 6\№2\Input.txt' , 'r') as f:
        data = f.read()
        data = data.split(',')
        C = int(data[0])
        H = int(data[1])
        O = int(data[2])
    print(f'Считаны следующие данные : C = {C}, H = {H}, O = {O}')
    
    while True:
        if (C >= 2) and (H >= 6) and (O >= 1): 
            molecule += 1
            C -= 2
            H -= 6
            O -= 1
        else: break

    with open('Homework 6\№2\Output.txt' , 'w') as f:
        f.write(f'Available number of molecules : {molecule}')

except IndexError: 
    print('Необходимо ввести три целых числа через запятую')

except ValueError:
    print('Необходимо ввести три целых числа через запятую')

except FileNotFoundError:
    print('Необходимо создать файл для чтения')