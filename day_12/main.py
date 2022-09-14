import mymodule
# or
# from mymodule import generate_full_name
import random
from string import ascii_letters, digits

print(mymodule.generate_full_name('Juan', 'López'))

def random_user_id() :
    caracteres_validos = ascii_letters + digits
    return ''.join(random.choices(caracteres_validos, k = 6))

print(random_user_id())

def user_id_gen_by_user() :
    number_of_characters = int(input("Introduce el número de caracteres de cada ID: "))
    number_of_ids = int(input("Introduce el número de IDs a generar: "))
    caracteres_validos = ascii_letters + digits
    ids = []
    for i in range(number_of_ids) :
        ids.append(''.join(random.choices(caracteres_validos, k = number_of_characters)))
    return ids

ids = user_id_gen_by_user()
for id in ids :
    print(id)

def shuffle_list(lista) :
    random.shuffle(lista)
    return lista
print(shuffle_list(["1", "2", "3", "7", "9", "11"]))

def random_numbers() :
    return random.sample(range(10), k = 7)
print(random_numbers())