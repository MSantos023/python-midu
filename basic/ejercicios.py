###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name="Manuel"
city= "Badajoz"
print(f"Mi nombre es {name}")
print(f"Y soy de {city}")
### FIN EJERCICIO 1

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"{a} es de tipo",type(a))
print(f"{b} es de tipo",type(b))
print(f"{c} es de tipo",type(c))
print(f"{d} es de tipo",type(d))
print(f"{e} es de tipo",type(e))
### FIN EJERCICIO 2

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
numero_a_transformar="12345"
numero_transformado=int(numero_a_transformar)
float_a_entero=3.99
print("Vamos a convertir ",numero_a_transformar," que es un ",type(numero_a_transformar),"en un entero.\n",numero_transformado,"Ahora es un tipo ", type(numero_transformado))
print("Lo que pasa si transformar ",float_a_entero,
      "\nes que elimina los decimales y deja el numero entero solo =>",int(float_a_entero))
### FIN EJERCICIO 3

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name2="Manuel"
age=33
altura = 1.80
print(f"Hola me llamo {name2}, tengo {age} y mido {altura}")
### FIN EJERCICIO 4

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI ")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
pi = 3.1416
pi_redondeado=round(pi)
print(f"El redondeo de pi es: {pi_redondeado}")
resultado=int(pi_redondeado/2)
print(f"el resultado de la division del redondeo de pi y el numero 2 es:",resultado)

### FIN EJERCICIO 5