# Como efectuar cálculos con tipos numéricos.

# Operadores aritméticos.
# Suma +, resta -, multiplicación *, división /.
print(4+5)
print(4-5)
print(4*5)
print(4/5)

# Inverso aditivo -, exponencición **, división entera //, módulo %.
print(-5)
print(4**5)
print(7//5)
print(7%5)

# Expresiones con más de un operador se evalúan por precedencia
# Las operaciones con igual precedencia se evaluan por orden de asociatibidad.
# **  precedencia 1
# +,- (unitarios) precedencia 2
# *,/,//,% precedencia 3
# +,- (binarios) precedencia 4

# Operadores de comparación.
# Siempre entregan un tipo bool y se aplican a valores numéricos.
# <, >=, >,>=, !=, ==.
print("menor 5<5.1:", 5 < 5.1)
print("mayor o igual 3>=5:", 3 >= 5)
print("distinto 3!=5:", 3 != 5)
print("igualdad 6==9:", 6==9)

# Operadores lógicos o booleanos
# Se aplican a bool y siempre entregan un tipo bool.
# not, and, or
print("negación not 3 > 5: ", not 3 > 5)
# Invierte el resultado de un valor lógico
print("conjunción lógica (y) 3 > 5 and 2 < 6:", 3 > 5 and 2 < 6)
# Entrega True sólo cuando ambos valores son verdaderos
print("disyunción lógica (o) 3 > 5 or 2 < 6:", 3 > 5 or 2 < 6)
# Entrega True cuando uno de los valores es verdadero.

# Operadores para tipos de texto
# +, *
print("concatenación Yo soy + tu padre:", "Yo soy " + "tu padre")
print("repetición ja + 4:", "ja " * 4)


