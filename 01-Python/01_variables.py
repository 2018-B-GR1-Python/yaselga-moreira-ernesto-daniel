##variables
print("Hola mundo")
edad: int = 20
sueldo: float =1.02
print(edad + sueldo)

nombre = "Ernesto" #comentario
apellido = 'Ernesto'
apellido_materno = """Ernesto"""

print(nombre == apellido)  # True / False
print(apellido == apellido_materno)  # True / False
print(apellido_materno)
print(int(True))  # 1
print(int(False))  # 0
print(str(True))  # True
print(str(False))  # False

print("ernesto yaselga".capitalize())  # Ernesto yaselga
nombre_completo = "ernesto yaselga".split(" ")  # ['ernesto', 'yaselga']
print(nombre_completo[0].capitalize() + " " + nombre_completo[1].capitalize())
print("Daniel".isalpha())  # True
print("Daniel10".isalpha())  # False
print("Daniel10".isnumeric())  # False
print("Daniel10".isalnum())  # True
print("10".isalnum())  # True
print("Daniel".isalnum())  # True
print("Daniel10--".isalnum())  # False
# print(int("vicente"))  # ERROR !
print("Mi nombre es {0} {1}".format(nombre_completo[0].capitalize(), "Yaselga"))
print(f"Mi nombre es {nombre_completo[0].capitalize()}"
      f"{nombre_completo[1].capitalize()}")
print(r"Saltos de linea \n as")  #raw
no_existe = None  #None = Null
print(no_existe)

