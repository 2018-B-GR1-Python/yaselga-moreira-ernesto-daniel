arregloNumeros = [1,2,3,4,5,6,7,8,9]

for numero in arregloNumeros:
    print(numero)

for x in range (0,5):
    print(f"Numero de iteracion: {x}")

for indice in range(7,12):
    print(f"Numero de iteracion: {indice}")

for indice in range(10):
    print(f"Numero de iteracion: {indice}")
    if(indice ==6 ):
        break  # Detener la ejecución del loop en el 6

for indice in range(10):
    if(indice ==6 or indice ==4):
        continue # Detener la ejecución del loop en el 6 y continua en el siguiente
    print(f"Numero de iteracion: {indice}")

numeroAuxiliar = 0

while numeroAuxiliar < 10:
    print(f"Numero: {numeroAuxiliar}")
    numeroAuxiliar += 1

numeroAuxiliarDos = 0
while True:
    print(f"Numero dos: {numeroAuxiliarDos}")
    numeroAuxiliarDos += 1
    if numeroAuxiliarDos == 70:
        break