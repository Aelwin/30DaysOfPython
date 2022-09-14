from operator import truediv
from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries :
    print(country)    
print("******************************************")
def sacar_por_pantalla(lista) :
    [print(elemento) for elemento in lista]
    print("******************************************")

countries_upper = map(lambda country : country.upper(), countries)
sacar_por_pantalla(countries_upper)
numbers_square = map(lambda number : number ** 2, numbers)
sacar_por_pantalla(numbers_square)
names = map(lambda name : name.upper(), names)
sacar_por_pantalla(names)

sacar_por_pantalla(filter(lambda country : 'land' in country, countries))
sacar_por_pantalla(filter(lambda country : len(country) == 6, countries))
sacar_por_pantalla(filter(lambda country : country[0] == 'E', countries))

def get_string_lists(lista) :
    return filter(lambda elemento : type(elemento) == str, lista)

sacar_por_pantalla(get_string_lists(['Juan', 2, 'López', 32.4, ['otra lista']]))

def add_two_nums(x, y):
    return int(x) + int(y)
print(reduce(add_two_nums, numbers))