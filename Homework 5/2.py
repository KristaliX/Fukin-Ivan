def sum (*digits) :
    try :
        s = 0
        for i in digits : s += i
        return s
    except TypeError : 
        print('Необходимо вводить только числа')
        return

print('Сумма равна : {}'.format(sum(1,2,3,4,5)))
print('Сумма равна : {}'.format(sum(1,2,3)))
print('Сумма равна : {}'.format(sum('a','b','c')))
print('Сумма равна : {}'.format(sum()))