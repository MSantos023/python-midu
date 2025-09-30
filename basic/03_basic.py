###
# 03_basic casting/conversion de tipos
# Transformar un tipo de dato en otro tipo de dato
###

print("Conversion de tipos de datos")

print("de str a int")

# Si intentaras print("10" + 5) obtendrias un error de tipo, te diria que estas intentado contactenar str con int
# Al reves lo mismo print(10 + "5"), te diria que estas intentando sumar int con str
# Si quieres sumar un str que contiene un numero con un int, tienes que convertir el str a int
print(int("10") + 5)  # Convierte el str "10" a int y luego suma 5

print("de int a str")
print("10" + str(5))  # Convierte el int 5 a str y luego concatena "10" con "5"
#print(int("sdfasdf")) obviamente esto da error porque no se puede convertir un str que no es un numero a int
#directamente te da error no es un numero, peta y da ValueError

print("de str a float")
print(float("10.5") + 5.5)  # Convierte el str

print("de float a int")
print(int(10.9) + 5)  # Convierte el float 10.9 a int (trunca el decimal) y luego suma 5, pero con esto pierdes precision
print(int(2.5)) # Convierte el float 2.5 a int (trunca el decimal) y da 2, porque no redondea, simplemente quita los decimales
print(round(2.5)) # Si quieres redondear usa round() y da 2 porque redondea al numero par mas cercano si es justo .5
print(round(3.5)) # Si quieres redondear usa round() y da 4 porque redondea al numero par mas cercano
print(round(2.6)) # Si quieres redondear usa round() y da 3 porque redondea al numero mas cercano
print(round(2.4)) # Si quieres redondear usa round() y da 2 porque redondea al numero mas cercano

print("int a bool")
print(bool(1))  # Convierte el int 1 a bool (True)
print(bool(0))  # Convierte el int 0 a bool (False) 0 es el unico int que es False
print(bool(-1))  # Incluso los negativos son True
print(bool("")) # Una cadena vacia es False
print(bool(" ")) # Cualquier cadena no vacia es True
print(bool("Hola")) # Cualquier cadena no vacia es True

