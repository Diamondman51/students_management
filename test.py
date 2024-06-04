from random import randint


def generate_randomNumber():
    number = randint(1, 1000)
    random_number = f'{number:04d}'
    return random_number

print(generate_randomNumber())