# while nos permite repetir tantas veces como queramos un conjunto de instrucciones.

#Programa para convertir de fahrenheit a celsius
# C = (F - 32)* 5/9
temp = 32
print("fº     cº")
while temp < 73:
    print(temp, "   ", int((temp - 32) * 5 / 9))
    temp = temp + 1

x = 48
y = 8
n = 0
while x > 0:
    x = x - y
    n = n + 1

print(48**8)
print(48//8)
