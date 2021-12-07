try :
    def xor(str , key) : # Посимвольное шифрование XOR 
        encrypt_str = ''
        for letter in str : encrypt_str += chr(ord(letter) ^ key) # Берём символ из str и шифруем его
        return encrypt_str 

    str = ''
    d_str = ''
    with open('Homework 6\№3\input.txt' , 'r') as f :
        str = f.read()
        print(f'Были считаны следующие данные : {str}')
    key = int(input('Введите ключ шифрования : '))
    str = xor(str , key)
    d_str = xor(str , key)
    with open('Homework 6\№3\output.txt' , 'w') as f :
        f.write(f'Encrypted string : {str} with key : {key}\n')
        f.write(f'Decrypted string : {d_str} with key : {key}')
except FileNotFoundError :
    print('Необходимо создать файл для чтения')
except UnicodeEncodeError :
    print('Невозможно закодировать с данным ключом, необходимо ввести меньший ключ')
except ValueError :
    print('В качестве ключа необходимо ввести целое положительное число')