# from random import randint
#
#
# def generate_randomNumber():
#     number = randint(1, 1000)
#     random_number = f'{number:04d}'
#     return random_number
#
# print(generate_randomNumber())

tpl = ('one', 'two', 'three')
tpl = ', '.join(tpl)
# print(tpl)


def pt(*args):
    print(f"Hush kelibsiz, {', '.join(args[:-1])}", args[-1], sep=' va ')


# pt('Anvar', 'Bekzod')
# pt('Anvar', 'Bekzod', 'Otabek')
# pt('Anvar', 'Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar')

# def info(**kwargs):
#     print(', '.join([f"{key} {value}" for key, value in kwargs.items()]))
#
# info(ismi="Otabek", familiyasi="Nuriddinov", yoshi=2)
# info(familiyasi="Nuriddinov", yoshi=20)
# info(ismi="Otabek", yashash_joyi='Toshkent')

def deco(f):
    def ichki(a, b):
        return