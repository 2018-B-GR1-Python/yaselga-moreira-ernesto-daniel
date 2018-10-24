def hola_mundo():  # funciones sin 'return' devuelve none
    print("Hola Mundo")

print(hola_mundo())

def sumar_dos_numeros(num_uno,num_dos):
    return num_uno+num_dos

print(sumar_dos_numeros(1.5,5))

def compara(num_uno,num_dos):
    if(num_uno==1):
        return "Hola"
    else:
        return num_uno+num_dos

print(compara(1,5))

def imprimir_universidad(nombre_universidad = "EPN"):  # parámetro por defecto
    print(f"{nombre_universidad} es lo maximo")

imprimir_universidad()

def guardar_carros(posicion,placa,usuario,tip,color):
    print(f"Guardamos en {posicion} el auto con placa {placa}"
          f" del usuario {usuario}")
    if (color):
        print(f"El carro es color {color}")
    if(tip):
        print(f"se recibió un tip de {tip}")

guardar_carros(1,"PSB-1022","Ernesto",None,None)
guardar_carros(tip=1.50,
               color="azul",
               posicion=2,
               placa="PXA-1506",
               usuario="Daniel")

# tipos de parámetros y posición de uso
# inicio    = posicional(normal)
# siguiente = predeterminados(=) | indefinidos(*)
# final     = kwargs(**)

def sumar_numeros(resta, *numeros, valor_inicial=0):  #recibe x parámetros, se interpera como tupla
    print(resta)
    print(numeros)
    print(valor_inicial)
    for numero in numeros:
        valor_inicial=valor_inicial+float(numero)
    return valor_inicial-resta

print(sumar_numeros(1,1,2,3,4,5,6,7,8,9,0,1,2,3,4, valor_inicial=10))

# kwaarg (key words arguments)

def imprimir_nombre(**kwargs):
    print(f" primer nonmre {kwargs['primer_nombre']} segundo nombre {kwargs['segundo_nombre']}"
          f" apellido paterno {kwargs['apellido_paterno']} apellido materno {kwargs['apellido_materno']}")

# imprimir_nombre("a","b","c","d") # type_error no se puede mandar argumentos posicionales con los kwargs
imprimir_nombre(primer_nombre="Ernesto",
                segundo_nombre="Daniel",
                apellido_paterno="Yaselga",
                apellido_materno="Moreira")


nombre = input("Ingrese su nombre")  # siempre devuelve un string

print(f"Usted ingreso: \"{nombre}\"")

numero = input("Ingrese numero")  # siempre devuelve un string
float(numero)
if (numero==1.5):
    print("Uno y medio")
else:
    print("Otra cosa")

opcional = input("Desea papas con su orden?, Opc:Si Opc:No")

if(True if opcional=="Si" else False):
    print("Truty")
else:
    print("Falsy")

numeros = input("Ingrese numeros")

numeros1 = numeros.split(",")

print(sumar_numeros(0,valor_inicial=0,*numeros1))

def calculadora(numero_uno,numero_dos,operacion="suma"):
    def sumar_dos_numeros():
        return numero_uno + numero_dos

    def restar_dos_numeros():
        return numero_uno - numero_dos

    def multiplicar_dos_numeros():
        return numero_uno * numero_dos

    def dividir_dos_numeros():
        return numero_uno / numero_dos

    def switch_operaciones():
        return {
            'suma':sumar_dos_numeros(),
            'resta':restar_dos_numeros(),
            'multi': multiplicar_dos_numeros(),
            'divide': dividir_dos_numeros()
        }[operacion]

    return switch_operaciones()

print(calculadora(3,4,operacion="suma"))
print(calculadora(3,4,operacion="resta"))
print(calculadora(3,4,operacion="multi"))
print(calculadora(3,4,operacion="divide"))

## proyecto de las 4 operaciones vásicas CREAR BORRAR ACTUALIZAR BUSCAR

# CONTROL DE PARADAS DE AUTOBUSES
# crear paradas (id, ubicacion (calle principal, calle secundaria), nombre, *lineas)
# editar informacion de paradas (nombre de las calles, agregar lineas quitar lineas )
# demoler paradas (por (id, nombre) )
# buscar paradas (por id, por nombre, por calles)
# consultar lineas de paradas (por id, por nombre, por calles)
# consultar paradas de una linea (linea)

#leer y escribir archivos

def leer_archivo(path):
    try:

        archivo_abierto = open(path)  #Predetrminado es 'r' que significa leer
        print("Si se pudo leer")

        arreglo_lineas_archivo = archivo_abierto.readlines()
        for linea in arreglo_lineas_archivo:
            print(linea)

        archivo_abierto.close()

    except Exception:
        print("No se pudo leer")



def escribir_archivo(path,*lineas_a_escribir):
    try:

        archivo_abierto = open(path,'a')  #Predetrminado es 'r' que significa leer

        for linea in lineas_a_escribir:
            archivo_abierto.write("\n"+linea)

        archivo_abierto.close()

    except Exception:
        print("No se pudo leer")

escribir_archivo('./08_ejemplo.txt',input("Escriba el texto a ingresar"))
leer_archivo('./08_ejemplo.txt')


elevar_cuadrado = lambda n:n*n
sumar_numeros_V2 = lambda x, y: x+y

print(elevar_cuadrado(5))
print(sumar_numeros_V2(34,87))