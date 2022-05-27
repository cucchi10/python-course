import json

#json.dumps --- enviar info

#json.loads --- recuperar info
# pasa todo a str (string)

entero = 33
json_entero = json.dumps(entero)
print(json_entero)
print(type(json_entero))

python_entero = json.loads(json_entero)
print(python_entero)
print(type(python_entero))

cadena = 'Hola Mundo'
json_cadena = json.dumps(cadena)
print(json_cadena)

python_cadena = json.loads(json_cadena)
print(python_cadena)

lista = [1, 2, 'tres']
json_lista = json.dumps(lista)
print(json_lista)
print(type(json_lista))

python_lista = json.loads(json_lista)
print(python_lista)
print(type(python_lista))

diccionario = {'entero':1, 'cadena':'Hola', 'lista':[1, 2, 'tres', 4.4]}
json_diccionario = json.dumps(diccionario)
print(json_diccionario)
print(type(json_diccionario))

python_diccionario = json.loads(json_diccionario)
print(python_diccionario)
print(type(python_diccionario))


with open('archivo_json.json', 'w') as archivo:
    json.dump(diccionario, archivo)

with open('archivo_json.json', 'r') as archivo:
    datos = json.load(archivo)