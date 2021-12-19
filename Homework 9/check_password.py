def check_password(a):
    """Функция принимает в качестве аргумента строку-пароль и проверяет её на условия:

    Должен быть не менее 6 символов;

    Должен содержать хотя бы одну цифру;

    Не должен состоять только из цифр;

    Не должен содержать слово “password” в любом регистре.
    
    Функция возвращает True или False. 
    """

    x = 0

    if len(a) >= 6: 
        for i in range(0 , len(a)):

            if a[i].isdigit(): x = x + 1;
            else: continue

        if(x == len(a)): return False

        elif(x  == 0): return False

        else:
            a = a.lower()
            if 'password' in a : return False 
            else: return True

    else: return False