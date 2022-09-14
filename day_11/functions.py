def add_two_numbers(param1, param2) :
    return param1 + param2
print(f"La suma de 3 y 4 es {add_two_numbers(3, 4)}")

def area_of_circle(radio) :
    return 3.14 * radio**2
print(f"El área de un círculo de radio 4 es {area_of_circle(4)}")

def add_all_nums(*numeros) :
    suma = 0
    for numero in numeros :        
        if type(numero) == int :
            suma += numero
        else :
            return "Hay valores que no son números"
    return suma
print(add_all_nums(3, 4, 5))
print(add_all_nums(3, 4, "5"))

def convert_celsius_to_fahrenheit(temperatura) :
    return (temperatura * 9/5) + 32

print(f"42ºC son {convert_celsius_to_fahrenheit(42)} fahrenheit")