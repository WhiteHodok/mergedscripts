import random
from mimesis import Person
from typing import List # Задаём нашу явную типизацию данных
'''
Структура кода соответствует требованиям Д.Грасса в его книге "Data Science наука о данных с нуля".
Уже более походит на формат Дзена в пайтоне.
'''
def generate_password(length: int) -> str:
    """Генерирует пароль длиной length"""
    chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = "".join(random.choice(chars) for _ in range(length))
    return password

def generate_email() -> str:
    """Генерирует случайный e-mail адрес"""
    person = Person('en')
    email = person.email(domains=['gmail.com'])
    return email

def generate_email_password_pairs(num_pairs: int, password_length: int) -> List[str]:
    """Генерирует num_pairs случайных пар e-mail:password"""
    pairs = []
    for _ in range(num_pairs):
        email = generate_email()
        password = generate_password(password_length)
        pair = f"{email}:{password}"
        pairs.append(pair)
    return pairs

# Пример использования
num_pairs = int(input("Введите количество пар: "))
password_length = int(input("Введите длину пароля: "))
pairs = generate_email_password_pairs(num_pairs, password_length)
for pair in pairs:
    print(pair)

