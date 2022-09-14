from audioop import reverse


lst = list()
lst = [] # Son equivalentes

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

enteros = [1, 2, 3, 4, 5, 6, 7]
print(len(enteros))
print(enteros[0], enteros[3], enteros[-1])

mixed_data_types = ["Juan", 38, 1.74, 'single', 'una calle']
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("There is", len(it_companies), "companies")
print(f"{it_companies[0]}, {it_companies[3]}, {it_companies[-1]}")
it_companies.append("Twitter")
it_companies.insert(4, "Instagram")
print(it_companies)
it_companies[1] = it_companies[1].upper()
print("#; ".join(it_companies))
print("Microsoft" in it_companies)
print(sorted(it_companies))
print(sorted(it_companies, reverse=True))
print(it_companies[0:3])
print(it_companies[-4:-1])
del it_companies[0]
del it_companies[-1]
it_companies.clear()
del it_companies # Elimina la variable
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack[5:2] = ["Python", "SQL"]
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"Min age is {ages[0]}")
print(f"Max age is {ages[-1]}")
ages.append(ages[0])
ages.append(ages[-1])
ages.sort()
print(ages)
longitud = len(ages)
if longitud % 2 == 0:
    print("Edades en la mitad", ages[int((longitud/2) - 1)], ages[int(longitud/2)])
else :
    print("Edad en la mitad", ages[longitud % 2])
print("La media es", sum(ages) / longitud)
print(f"El rango de edades está entre {ages[0]} y {ages[-1]}")

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(scandic)