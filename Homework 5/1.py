def check_password(s) :
    x = 0
    if len(s) < 6 : 
        print('Пароль должен быть не менее 6 символов')
        return False
    for i in s :
        if i.isdigit() : x += 1
    if x == len(s) :
        print('Пароль не должен состоять только из цифр')
        return False
    if x == 0 :
        print('Пароль должен содержать хотя бы 1 цифру')
        return False
    s = s.lower()
    if 'password' in s :
        print('Пароль не должен содержать "password" в любом регистре')
        return False
    return True

s = 0
s = input('Введите строку-пароль : ')
s = check_password(s)
print('Результат проверки вашего пароля : {}'.format(s))