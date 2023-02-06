def encrypt():
    text = input('Please enter text you want to encrypt')
    print('Your encrypted text:')
    if language == 'eng':
        for i in text:
            if i.isalpha():
                encrypted_chr = ord(i) + int(shear_step)
                if (91 > ord(i) > 64 and encrypted_chr > 90) or (123 > ord(i) > 96 and encrypted_chr > 122):
                    encrypted_chr -= 26
                print(chr(encrypted_chr), end='')
            else:
                print(i, end='')
    else:
        for i in text:
            if i in rus_lower_alphabet:
                new_index = (rus_lower_alphabet.index(i) + int(shear_step)) % 32
                print(rus_lower_alphabet[new_index], end='')
            elif i in rus_upper_alphabet:
                new_index = (rus_upper_alphabet.index(i) + int(shear_step)) % 32
                print(rus_upper_alphabet[new_index], end='')
            else:
                print(i, end='')


def decrypt():
    text = input('Please enter text you want to decrypt')
    print('Your decrypted text:')
    if language == 'eng':
        for i in text:
            if i.isalpha():
                decrypted_chr = ord(i) - int(shear_step)
                if (91 > ord(i) > 64 and decrypted_chr < 65) or (123 > ord(i) > 96 and decrypted_chr < 97):
                    decrypted_chr += 26
                print(chr(decrypted_chr), end='')
            else:
                print(i, end='')
    else:
        for i in text:
            if i in rus_lower_alphabet:
                new_index = (rus_lower_alphabet.index(i) - int(shear_step)) % 32
                print(rus_lower_alphabet[new_index], end='')
            elif i in rus_upper_alphabet:
                new_index = (rus_upper_alphabet.index(i) - int(shear_step)) % 32
                print(rus_upper_alphabet[new_index], end='')
            else:
                print(i, end='')


print('Welcome to Caesar Cipher!')

action = input('Enter please what you want to do: encrypt or decrypt').lower()
while action != 'encrypt' and action != 'decrypt':
    action = input('Please enter valid answer (encrypt/decrypt)').lower()

language = input('Choose language: ru or eng').lower()
while language != 'ru' and language != 'eng':
    language = input('Please enter valid answer (ru/eng)').lower()
if language == 'ru':
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

shear_step = input('Enter shear step')
while not shear_step.isdigit():
    shear_step = input('Please enter valid integer number')

if action == 'encrypt':
    encrypt()
elif action == 'decrypt':
    decrypt()
