# Print nos permite mostrar en pantalla los datos
pesos_por_hora = 200
llegada = 19
salida = 20
precio = (salida - llegada) * pesos_por_hora
print(precio, "pesos")

# Podemos imprimir el resultado de expresiones
print((3 + 5 // 4 - 2) - 2 ** 4 + 3 * (7 - 2))

# Podemos imprimir variables calculadas previamente
fahrenheit = 91
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)

# Imprimir exprersiones con variables
temperatura = 33
print(temperatura >= 30)

# Para imprimir multiples expresiones las separamos por comas
episodio = 3
print("Episodio", episodio, "del libro")

# end= mantiene las expresiones en la misma linea
nombre = "yo"
edad = 40
print("soy", nombre, end="")
print("y tengo", edad, "años")
print("cumplidos")
# Podemos añadir un texto en el end
print("Este print", end=" :D ")
print("no cambia", "de línea")
# sep permite cambiar el separador de expresiones
print("el tesoro", "está", "en", sep="...")
