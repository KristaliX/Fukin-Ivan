def xor(str, key):
    """Функция принимает в качестве аргумента строку и ключ (целое число).
    
    Функция возвращает XOR-кодировку переданной строки с использованием ключа.
    """ 
    try: 
        encrypt_str = ''
        for letter in str: encrypt_str += chr(ord(letter) ^ key) 
        return encrypt_str

    except ValueError:
        print('В качестве ключа необходимо ввести целое положительное число')

    except UnicodeEncodeError:
        print('Невозможно закодировать с данным ключом, необходимо ввести меньший ключ')

str = ''
d_str = ''

with open('Homework 6\№3\input.txt' , 'r') as f:
    try:
        str = f.read()
        print(f'Были считаны следующие данные : {str}')
        key = int(input('Введите ключ шифрования : '))
        str = xor(str, key)
        d_str = xor(str, key)

    except FileNotFoundError:
        print('Необходимо создать файл для чтения')

with open('Homework 6\№3\output.txt' , 'w') as f:
    f.write(f'Encrypted string : {str} with key : {key}\n')
    f.write(f'Decrypted string : {d_str} with key : {key}')