###
# 04_basic Variables
# Las variables sirven para guardar datos en memoria y poder reutilizarlos
# python es un lenguaje de tipado dinamico y de tipado fuerte
# Tipado dinamico: no hace falta declarar el tipo de dato de una variable, python lo infiere automaticamente
# Tipado fuerte: no se pueden mezclar tipos de datos sin convertirlos
###


# para asignar variables se usa el operador =
my_name = "manue"
print(my_name)

my_age = 30
print(my_age)

# Puedo reasignar variables
my_age = 33
print(my_age)


# Tipado dinamico: se determina en tiempo de ejecucion, no tienes que declararlo explicitamente
# basicamente puede cambiar segun se va ejecutando

my_variable = "Hola"
print(my_variable)
# se le vuelve a reasignar un int y cambia de tipo
my_variable = 10
print(my_variable)

# Tipado fuerte: python no hace cambios de tipo automaticos
#print(123423 +"33") # da error porque no puedes sumar un int con un str

# f-strings: forma de formatear cadenas de texto, pero no ha estado siempre en python
# se introdujo en python 3.6, si usas una version anterior no funciona
my_name = "manue"
my_age = 30
print(f"Me llamo {my_name} y tengo {my_age} años")  # f antes de la cadena indica que es una f-string

# forma no recomendada de asiganr variables
name, age , city = "manue", 33, "badajoz"
print(f"Me llamo {name}, tengo {age} años y vivo en {city}")

# Como si nombrar variables que tienen varias palabras o espacios
# se usa snake_case (guion bajo) o camelCase (mayuscula en la segunda palabra)
# las dos valen, pero la mas usada en python es snake_case
my_full_name = "manuel santos"
myFullName = "manuel santos"

# python no tiene constantes en la sintaxis de variables se puede simular con diferentes cosas pero se usan mayusculas para decir que es una constante.
CONSTANTE = "valor constante"
print(CONSTANTE)

# empezar variables con numeros no es valido 1241234_numero
# mi-variable con guion no es valido
# mi variable con espacio no es valido  
# mi@variable con simbolos no es valido
#tampoco puede usar palabras reservadas de python como variable (if, else, for, while, def, return, import, from, as, etc)

# anotacion de tipos (type hinting)
# no es obligatorio pero ayuda a entender el codigo y a herramientas de analisis estatico
# si usas las anotaciones despues, incluso los anteriores te dara error porque los vuelve estaticos

is_user_loggedin: bool = True
print(is_user_loggedin)
# no hace falta poner la anotacion de tipos, python lo infiere automaticamente
# is_user_loggedin = 2
# print(is_user_loggedin)