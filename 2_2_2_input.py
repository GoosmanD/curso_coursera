# input nos permite preguntarle datos al usuario
nombre = "Dr. Nick"
saludo = "Hola, "
pregunta = "¿Cómo estás hoy?"
print(saludo, nombre, pregunta)

nombre = input("¿Cúal es tu nombre?")
saludo = "Hola, "
pregunta = "¿Cómo estás hoy?"
print(saludo, nombre, pregunta)

# input da string, para convertirlo a un número lo tenemos convertir a un entero con int
lec = int(input("¿Cúantas lecciones has visto? "))
total = 15
faltan = total - lec
print("Te faltan ", faltan, "lecciones, ¡Ánimo!")

# Podemos convertir a int, float, bool.
#int
monedas = int(input("¿Cuántas monedas tienes"))
siguiente = monedas + 1
print("Yo tengo más. Tengo", siguiente)
#float
t = float(input("¿En cuantos segs corres 100 m"))
dif = t - 9.58
print("Eres ", dif, "segundos más lento que Bolt" )
#bool
ingreso = bool(input("Ingresa tu nombre: "))
print("Nombre ingresado: ", ingreso)

