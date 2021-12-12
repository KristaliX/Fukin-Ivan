def fibonacci(n):
    """Функция принимает в качестве аргумента индекс (целое число)

    Функция возвращает число Фибоначчи с этим индексом. 
    """

    if n == 0: return 0

    if n in (1, 2): return 1

    if n < 0: return fibonacci(n + 2) - fibonacci(n + 1)

    return fibonacci(n - 1) + fibonacci(n - 2)

def sum(*digits):
    """Функция находит сумму переданных аргументов и возвращает её."""

    try:
        s = 0
        for i in digits: s += i
        return s
    
    except TypeError: 
        print('Необходимо вводить только числа')
        return

def check_password(s):
    """Функция принимает в качестве аргумента строку-пароль и проверяет её на условия:

    Должен быть не менее 6 символов;

    Должен содержать хотя бы одну цифру;

    Не должен состоять только из цифр;

    Не должен содержать слово “password” в любом регистре.
    
    Функция возвращает True или False. 
    """

    x = 0

    if len(s) < 6: 
        print('Пароль должен быть не менее 6 символов')
        return False

    for i in s:
        if i.isdigit(): x += 1

    if x == len(s):
        print('Пароль не должен состоять только из цифр')
        return False

    if x == 0:
        print('Пароль должен содержать хотя бы 1 цифру')
        return False

    s = s.lower()
    
    if 'password' in s:
        print('Пароль не должен содержать "password" в любом регистре')
        return False
    return True