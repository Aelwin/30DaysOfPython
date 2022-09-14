from turtle import pu

"""
age = int(input("Introduzca su edad: "))
if age >= 18 :
    print("You are old enough to learn to drive.")
else :
    print(f"You need {18-age} more years to learn to drive.")

mi_edad = int(input("Introduce mi edad: "))
tu_edad = int(input("Introduce tu edad: "))
diferencia = mi_edad-tu_edad
if diferencia > 0 :
    print(f"Tengo {diferencia} {'año' if diferencia == 1 else 'años'} más que tú")
elif diferencia < 0:
    diferencia = abs(diferencia)
    print(f"Tienes {diferencia} {'año' if diferencia == 1 else 'años'} más que yo")
else :
    print("Tenemos la misma edad")

puntuacion = int(input("Introduce tu puntuación: "))
if puntuacion < 50 :
    print("Tu nota es F")
elif puntuacion >= 50 and puntuacion < 60 :
    print("Tu nota es D")
elif puntuacion >= 60 and puntuacion < 70 :
    print("Tu nota es C")
elif puntuacion >= 70 and puntuacion < 80 :
    print("Tu nota es B")
else :
    print("Tu nota es A")
"""
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 25,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person :
    print(person['skills'][2])
    print("Python" in person["skills"])
if person["is_married"] and person["age"] > 20 :
    print(f"{person['first_name']} {person['last_name']} has more than 20 years old. He is married")
