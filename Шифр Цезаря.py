alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmopqrstuvwxyzАБВГДЕЄЖЗИІЇйКЛМНОПРСТУФЧЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцшщбюяАБВГДЕЄЖЗИІЇйКЛМНОПРСТУФЧЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцшщбюя01234567890123456789"

encrypt = input("Введіть ваше речення: ")
key = int(input("Будь-ласка введіть ключ (цифру 1-25): "))
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print("Ваше зашифроване речення: ", encrypted)