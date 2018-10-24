tupla = (1,2,3,2,5,2,3,6,"a","b","c","c")
print(tupla)
for numeros in tupla:
    print(f"Numero {numeros}")

print(tupla.index(3))  #devuelve el índice del valor de una tupla

print(tupla.count(2))  #devuelve el numero de ocurrencias del valor

print(tupla[2])  #imprime el valor de la posicion

# tupla[0]=1 las tuplas no se pueden editar

print(set(tupla))  #devuelve la tupla sin repetidos