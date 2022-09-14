# A tuple is a collection of different data types which is ordered and unchangeable (immutable)
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

brothers = ("Javi", "Xabi", "Julen")
sisters = ("Iratxe", "Miren")
siblings = brothers + sisters
print(f"I have {len(siblings)} siblings")
siblings = list(siblings)
fathers = ["Paquita", "Amador"]
siblings.join(fathers)
family_mebers = siblings
print(family_mebers)