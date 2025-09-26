###
# 01_basic tipo de datos
# En python hay varios tipos de datos basicos.
# int -> enteros, float -> decimales,complex -> numero complejos, str -> cadenas de texto, bool -> booleanos (True o False),
# noneType -> nulo, list -> listas, tuple -> tuplas, dict -> diccionarios, range -> rangos, set -> conjuntos etc..
###

# Enteros
print("Enteros o int:")
print(10)
print(-123)
print(0)
print("Python tiene una funcion propia para saber el tipo de dato que es una variable o un valor que es type()")
print("Es tipo: ",type(10))

print("Float o decimales:")
print(10.5)
print(-0.1)
print(0.0)
print("Es tipo: ", type(10.5))

print("numeros complejos o complex:")
print(3 + 5j)   
print(2 - 3j)
print("Es tipo: ", type(3 + 5j))

print("Cadenas de texto o str:")
print("Hola Mundo")
print('Hola Mundo')
print("1")
print("Es tipo: ", type("Hola Mundo"))

print("Booleanos o bool:")
print(True)
print(False)
print(1 == 1)  # True
print(1 < 2)  # False
print("Es tipo: ", type(True))

print("NoneType o nulo:")
print(None)  # Representa la ausencia de valor
print("Es tipo: ", type(None))