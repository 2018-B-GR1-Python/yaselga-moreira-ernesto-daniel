ernesto = {
    "nombre":"Ernesto"
}
arregloNumeros = [1,2,3,4,5,6,7,8,9]

try:
    arregloNumeros["0"] = 55
except KeyError:  #para llaves mal puestas
    print("Error en la llave")
except TypeError: #
    print("Error Types")


