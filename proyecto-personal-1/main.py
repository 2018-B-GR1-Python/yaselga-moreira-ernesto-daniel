paradas=[[0,"La Magdanlena","Mariscal Sucre","Huaynapalcon",1,3,4,5,6],
         [1,"La Mascota","Mariscal Sucre","Rodrigo de Chavez",1,2,3,4,5,6],
         [2,"Los Dos Puentes S/N","Necochea","Francisco Barba",1,2,3,4,5,6],
         [3,"Los Dos Puentes N/S","Bahía","Francisco Barba",1,2,3,4,5,6],
         [4,"San Diego", "Mariscal Sucre", "Bahía",1,2,3,4,5,6]]

lineas_de_bus_dic={
    1:"R1",
    2:"R2",
    3:"R4",
    4:"R5",
    5:"R9",
    6:"R10B",
    7:"R11",
    8:"R12",
    9:"R13",
    10:"R14",
    11:"R15",
    12:"R17",
    13:"R18",
    14:"R19",
    15:"R20",
    16:"R21"
}


def main():
    opc1 = "99"
    while(opc1!=0):
        opc1 = "99"
        opc2 = "99"
        print("--" * 5, " Menu principal", "--" * 5)
        for llave, valor in menu_principal.items():
            print(f"{llave}.- {valor}")
        opc1 = int(input("Escoja la opcion deseada"))
        if(opc1 == 1):
            print(f"opcion escogida {opc1}")
            ingresar_parada(input("numero:"),
                            input("nombre: "),
                            input("calle principal: "),
                            input("calle secundaria: "),
                            input("lineas de bus separadas por comas: "))
        elif (opc1 == 2):
            print(f"opcion escogida {opc1}")
            while (opc2 != 0):
                print("--" * 5," Menu consulta ","--"*5)
                for llave, valor in menu_consultar.items():
                    print(f"{llave}.- {valor}")
                opc2 = int(input("Escoja la opcion deseada"))
                if (opc2 == 1):
                    consultar_parada()
                elif (opc2 == 2):
                    consultar_linea_de_bus()
                elif (opc2 == 3):
                    consultar_linea_parada()
        elif (opc1 == 3):
            editar_parada(input("numero:"),
                            input("nombre: "),
                            input("calle principal: "),
                            input("calle secundaria: "),
                            input("lineas de bus separadas por comas: "))

        elif (opc1 == 4):
            eliminar_parada(input("Ingrese el numero de la parada"))
menu_principal = {
    1: "Ingresar Parada",
    2: "Consultar",
    3: "Editar Parada",
    4: "Borrar Parada",
    0: "Salir"
}

menu_consultar = {
    1: "Consultar Paradas",
    2: "Consultar Lineas de bus",
    3: "Consultar Lineas de bus en la parada",
    0: "Salir"
}

def ingresar_parada(numero,nombre,callep,calles ,lineas):
    paradas.append([int(numero),nombre,callep,calles])
    print(lineas)
    numeros = lineas.split(",")
    print(numeros)
    for num in numeros:
        paradas[int(numero)].append(int(num))
    #print(paradas)

def consultar_parada():
    print("--" * 5, " PARADAS", "--" * 5)
    for parada in paradas:
        print("#",parada[0],"| \tNombre: ",parada[1],"| \tCalle Principal: ",parada[2],"| \tCalle secundaria: ",parada[3])
    print("\n")

def consultar_linea_de_bus():
    print("--" * 5, " LINEAS DE BUS ", "--" * 5)
    for linea in lineas_de_bus_dic.items():
        print(f"Ruta: {linea}")
    print("\n")

def consultar_linea_parada():
    parada = int(input("Ingrese el # de la parada"))
    for lineas in (paradas[parada][4:]):
        print(f"Linea:{lineas_de_bus_dic[lineas]}")

def editar_parada(numero,nombre,callep,calles ,lineas):
    paradas.pop(int(numero))
    paradas.append([int(numero), nombre, callep, calles])
    print(lineas)
    numeros = lineas.split(",")
    print(numeros)
    for num in numeros:
        paradas[int(numero)].append(int(num))
    # print(paradas)

def eliminar_parada(numero):
    paradas.pop(int(numero))
    print(f"Parada {numero} borrada")

def eliminar_parada_todo():
    pass

main()
