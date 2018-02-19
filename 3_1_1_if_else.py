# Haremos que el programa tome decisiones dependiendo de si una condición es verdadera o falsa.
# Una condición puede tener dos valores, verdadero o falso.
# Operadores ariitméticos
print(5 < 5.1)
print(3 >= 5)
print(3 != 5)
print(6 == 9)

# Operadores lógicos not, and or.
print("negación 3 > 5", not 3 > 5)
print("Conjunción lógica Y 3 > 5 and 2 < 6", 3 > 5 and 2 < 6)
print("Disyunción lógica O 3 > 5 or 2 < 6", 3 > 5 or 2 < 6)

# Instrucción condicional
# If condición:
#   instrucción1
# else:
#   Instrucción2

llueve = True
if llueve == True:
    print("Llevaré paraguas")
else:
    print("no llevaré paraguas")
print("ahora saldré a la calle")

llueve = False
if llueve == True:
    print("Llevaré paraguas")
else:
    print("no llevaré paraguas")
print("ahora saldré a la calle")

