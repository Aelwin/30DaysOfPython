age = 38
height = 1.73
complexNumber = 1 + 2j

triangle_height = float(input('Introduce la altura del triángulo: '))
triangle_base = float(input('Introduce la base del triángulo: '))
triangle_area = 0.5 * triangle_height * triangle_base
print('El área del triángulo es', triangle_area)

triangle_side1 = float(input('Introduce el primer lado del triángulo: '))
triangle_side2 = float(input('Introduce el segundo lado del triángulo: '))
triangle_side3 = float(input('Introduce el tercer lado del triángulo: '))
triangle_permiter = triangle_side1 + triangle_side2 + triangle_side3
print('El perímetro del triángulo es', triangle_permiter)

rectangle_side1 = float(input('Introduce el primer lado del rectángulo: '))
rectangle_side2 = float(input('Introduce el segundo lado del rectángulo: '))
rectangle_perimeter = 2 * (rectangle_side1 + rectangle_side2)
rectangle_area = rectangle_side1 * rectangle_side2
print('El área del rectángulo es', rectangle_area)
print('El perímetro del rectángulo es', rectangle_perimeter)

pi = 3.14
circle_radius = float(input('Introduce el radio del círculo: '))
circle_area = pi * circle_radius ** 2
circle_perimeter = 2 * pi * circle_radius
print('El área del círculo es', circle_area)
print('El perímetro del círculo es', circle_perimeter)

python = 'python'
dragon = 'dragon'
contiene = 'on' in python and 'on' in dragon
longitud_float = float(len(python))
longitud_string = str(longitud_float)
print("La longitud de la cadena", python, "es ", longitud_float, "en formato float y", longitud_string, "en formato string")

number = int(input("Introduce un número entero: "))
es_par = False
if number % 2 == 0 :
    es_par = True
print("¿El número", number, "es par?", es_par)

print("¿Es igual la 'floor division' de 7 entre 3 que convertir a entero 2.7?", 7//3 == int(2.7))
print("¿Es igual el tipo de '10' que el de 10?", type('10') == type(10))
print("¿Es igual convertir a entero 9.8 que 10?", int(9.8) == 10)

hours = int(input("Introduce las horas: "))
rate_per_hour = int(input("Introduce la ganancia por hora: "))
weekly_earnings = hours * rate_per_hour
print("Tus ganancias semanales son", weekly_earnings)

number_of_years = int(input("Introduce el número de años que has vivido: "))
seconds_in_years = number_of_years * 365 * 24 * 60 * 60
print("Has vivido", seconds_in_years, "segundos")