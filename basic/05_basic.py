###
# 05_basic Input
# La funcion input permite al usuario introducir datos por consola
###


print("¿Cual es tu nombre?")
name = input()
print(f"Hola {name}, bienvenido a python")

print("¿Cual es tu edad?")
age = input()
print(f"Tienes {age} años")
print(f"El año que viene tendras {int(age) + 1} años")  # input devuelve un str, hay que convertirlo a int para hacer operaciones matematicas
# si no conviertes age a int, la operacion sera una concatenacion de strings

print("Como obtener varios valores desde un solo input")
country, city= input("¿De que pais y ciudad eres?").split()

print(f"Entonces eres {name}, tienes {age} años y eres de {city}, {country}")