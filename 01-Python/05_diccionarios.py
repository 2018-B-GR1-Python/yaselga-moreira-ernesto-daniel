diccionario = {
    "nombre":"Ernesto",
    "apellido":"Yaselga",
    "edad":21,
    "sueldo":300.50,
    "hijos":[],
    "estado_civil":False,
    "loteria":None,
    "mascota": {"nombre":"Veci","edad":1}
}

print(diccionario)

print(diccionario["nombre"])
print(diccionario.get("apellido"))
print(diccionario["mascota"]["nombre"])
diccionario.pop("estado_civil")
print(diccionario)
print(diccionario.values())

for valor in diccionario.values():
    print(valor)

for llave in diccionario.keys():
    print(f"Llave: {llave} \tvalor: {diccionario.get(llave)}")

for llave, valor in diccionario.items():
    print(f"Llave: {llave} valor: {valor}")

diccionario["profesion"]="estudiante"
print(diccionario)