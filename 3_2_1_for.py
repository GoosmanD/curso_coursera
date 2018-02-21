# Con for podemos conseguir que el programa repita una instrucción un número definido de veces.

print("fº     cº")
for temp in range(21):
    print(temp, "   ", int((temp - 32) * 5 / 9))

# Usamos una nueva expresión: range(fin)
#Range crea una secuencia de números, que parte desde cero y llega a fin -1


for i in range(7):
    print(i)

for z in range(11):
    print(z * 10)

# Tambien se puede poner un rango de numeros.

for v in range(10, 21):
    print(v)

# Podemos poner tres parametros (inicio, fin y paso) crea una secuencia de números, que parte desde el inicio
# y llega hasta fin -1 avanzando de a paso números.

for a in range(0,11,2):
    print(a)
