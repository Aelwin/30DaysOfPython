# Set is a collection of unordered and un-indexed distinct elements
st = {}
# or
st = set()

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter") # Un elemento
it_companies.update(["Instagram", "Apache"]) # Múltiples elementos
print(it_companies)

it_companies.remove("Facebook") # Si no existe da error
it_companies.discard("No existe") # No da error si no existe

A.union(B)
A.intersection(B)
print(A.issubset(B))