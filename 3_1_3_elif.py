# Si llueve y hace frío iré con paraguas y abrigado. Si sólo hace frío saldré abrigado.
# Si ni hace frío ni llueve saldré sin abrigo ni paraguas.

llueve = True
temperatura = int(input("Ingresa temperatura en grados centígrados"))
if temperatura < 18:
    if llueve == True:
        print("Llevaré partaguas y abrigo")
    else:
        print("Solo llevaré abrigo")
else:
    print("No necesito ni paraguas ni abrigo")

# if condición 1:
#   instrucción1
# elif condición2:
#   instrucción 2
# else:
#   instrucción3

llueve = True
temperatura = int(input("Ingresa temperatura en grados cntígados: "))
if temperatura < 18 and llueve == True:
    print("Llevaré paraguas y abrigo")
elif temperatura > 18 and llueve == False:
    print("Sólo llevaré abrigo")
else:
    print("No llevaré ni paraguas nio abrigo")
