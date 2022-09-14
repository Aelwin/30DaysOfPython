def filter_negatives_and_zero(lista) :
    return [i for i in lista if i <= 0]
print(filter_negatives_and_zero([-4, -3, -2, -1, 0, 2, 4, 6]))

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
intermediate_list = [number for row in list_of_lists for number in row]
flattened_list = [number for row in intermediate_list for number in row]
print(flattened_list)

numbers = [(i, 1, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(numbers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [list(map(lambda name: name.upper(), list(country))) for row in countries for country in row]
#flattened_countries = [row.insert(1, "FIN") for row in flattened_countries]
print(flattened_countries)
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# NO SOY CAPAZ DE INCLUIR LA CADENA EN EL MEDIO