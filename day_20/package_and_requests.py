import requests
import json

url = 'https://dsedeelectronica.vitoria-gasteiz.org/j03-01s/consulta/ND/paises/recuperar'  # countries api
response = requests.get(url, verify=False)
countries = response.json()["lista"]
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url, verify=False)
countries = response.json()
print(countries[:1])

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url, verify=False)
cats_json = response.json()
if response.status_code == 200 :
    cats = json.loads(response.text)
    #El peso en formato metrico viene en un rango. Ejemplo: 3 - 9
    cats_ordered_by_min_weight = sorted(cats, key=lambda cat: int(cat['weight']['metric'].split(' - ')[0]))
    cats_with_min_weight = list(filter(lambda cat : cat['weight'] == cats_ordered_by_min_weight[0]['weight'], cats_ordered_by_min_weight))
    print(f"Gatos con el peso más bajo({cats_with_min_weight[0]['weight']['metric'].split(' - ')[0]} Kg):")
    [print(cat['name']) for cat in cats_with_min_weight]
    
    print()

    cats_ordered_by_max_weight = sorted(cats, key=lambda cat: int(cat['weight']['metric'].split(' - ')[1]), reverse=True)
    cats_with_max_weight = list(filter(lambda cat : cat['weight'] == cats_ordered_by_max_weight[0]['weight'], cats_ordered_by_max_weight))
    print(f"Gatos con el peso más alto({cats_with_max_weight[0]['weight']['metric'].split(' - ')[1]} Kg):")
    [print(cat['name']) for cat in cats_with_max_weight]
else :
    print("Ha ocurrido un error recuperando la lista de gatos")