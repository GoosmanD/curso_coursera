# Usamos str para pasar un entero a un string
print(str(15))
print(type(str(15)))
print("Son las " + str(3 + 12))

# Usamos int para pasar de float a integer eliminando los decimaleso de string a integer.
print(int(3.05))
print(int("3") + 12)

# Usamos float para pasar un dato a float ya sea integer o string
print(float("3"))
print(float("3.5") + 12)

# Tambien podemos hacer conversiones a bool
# 0 ó "" es False, el resto es True
print(bool(0))
print(bool(""))
print(bool(15.5))
print(bool("True"))
print(bool("False"))
print(bool("0"))

# Podemos convertir cualquier valor numérico a string poniendo str
print(str(3.0))
print(str(8 + 1.76) + " segundos")
print(str(3 < 5 and 9.76 < 10))


