def encrypt():
    print('Your encrypted text:')
    if language == 'eng':
        for i in text:
            if (91 > ord(i) > 64) or (123 > ord(i) > 96):
                encrypted_chr = ord(i) + int(shear_step)
                if (91 > ord(i) > 64 and encrypted_chr > 90) or (123 > ord(i) > 96 and encrypted_chr > 122):
                    encrypted_chr -= 26
                print(chr(encrypted_chr), end='')
            else:
                print(i, end='')


def decrypt():
    print('Your decrypted text:')
    if language == 'eng':
        for i in text:
            if (91 > ord(i) > 64) or (123 > ord(i) > 96):
                decrypted_chr = ord(i) - int(shear_step)
                if (91 > ord(i) > 64 and decrypted_chr < 65) or (123 > ord(i) > 96 and decrypted_chr < 97):
                    decrypted_chr += 26
                print(chr(decrypted_chr), end='')
            else:
                print(i, end='')


print('Welcome to Caesar Cipher!')

action = input('Enter please what you want to do: encrypt or decrypt')
while True:
    if action == 'encrypt' or action == 'decrypt':
        break
    else:
        action = input('Please enter valid answer (encrypt/decrypt)')

language = input('Choose language: ru or eng')
while True:
    if language == 'ru':
        rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        break
    elif language == 'eng':
        break
    else:
        language = input('Please enter valid answer (ru/eng)')

shear_step = input('Enter shear step')
while True:
    if shear_step.isdigit():
        break
    else:
        action = input('Please enter valid integer number')

if action == 'encrypt':
    text = input('Please enter text you want to encrypt')
    encrypt()
elif action == 'decrypt':
    text = input('Please enter text you want to decrypt')
    decrypt()
