def fibonacci (n) :
    if n == 0 : return 0
    if n in (1,2) : return 1
    if n < 0 : return fibonacci(n+2) - fibonacci(n+1)
    return fibonacci(n-1) + fibonacci(n-2)
    
try :
    x = int(input('Введите число Фибоначчи : '))
    x = fibonacci(x)
    print('Ваше число Фибоначчи : {}'.format(x))
except ValueError :
    print('Необходимо вводить целое число')