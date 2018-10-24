arreglo = []

arregloNumeros = [1,2,3,4,5,6,7,8,9]

arregloCosas = [
    "abc",
    1,
    True,
    False,
    None,
    10.1,
    [1,2,3]
]

print(arregloNumeros[0:5])  # [0,3[ intervalo cerrado, intevalo abierto (no imprime el 6)
print(arregloNumeros[3:5])  # # se imprime desde el tercero hasta el uno antes del quinto
print(arregloNumeros[:2])  # se imprime desde el primero hasta el segundo
print(arregloNumeros[2:])  # se imprime desde el segundo hasta el ultimo
print(arregloNumeros[-2])  # se imprime el ultimo "menos X"
print(arregloNumeros[2:-2])  # se imprime hasta el ultimo "menos X"

print(15 in arregloNumeros)  # devuelve un booleano
print(5 in arregloNumeros)  # devuelve un booleano
print(len(arregloNumeros))  # devuelve el tamaños del arreglo

arregloNumeros.append((10)) # agrega un valor al final de la lista
print(arregloNumeros)

arregloNumeros.pop(9) # elimina el elemento en la posicion x de la lista
print(arregloNumeros)

arregloNumeros.insert(1,1.2)  # agrea un elemento Y en la posicion X
print(arregloNumeros)

del arregloNumeros[1:4]  # elimina un rango de elementos
print(arregloNumeros)