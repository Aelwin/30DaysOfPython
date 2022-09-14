language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

pto = language[0:6:2] # It is possible to skip characters while slicing by passing step argument to slice method.
print(pto) # Pto

cadena = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(cadena)
cadena2 = ' '.join(['Coding', 'For' , 'All'])
print(cadena2)
company = "Coding For All"
print(company)
print(f"Su longitud es {len(company)}")
print(company.upper()) # Todo mayúsculas
print(company.lower()) # Todo minúsculas
print(company.capitalize()) # Pone la primera letra en mayúsculas y el resto en minúsculas
print(company.title()) # Pone la primera letra de cada palabra en mayúsculas
print(company.swapcase()) # Cambia mayúsculas por minúsculas y viceversa
print(company[7:])
print(company.find('Coding') != -1)
print(company.replace('Coding', 'Python'))
print(company.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[10])

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %d meters square." %(radius, area))
print("The area of a circle with radius {} is {} meters square.".format(radius, area))
print(f"The area of a circle with radius {radius} is {area} meters square.")
