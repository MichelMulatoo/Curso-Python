#Ejemplos de Ciclo While

# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')

# minimo = 1
# contador = 7
#
# while contador >= minimo:
#     print(contador)
#     contador -= 1
# else:
#     print('Fin ciclo while  ')


altura = int(input("Ingresa la altura del triangulo: "))

i = 1
j = 1
for i in range(altura):
    for j in range(i):
        print(" * ", end = "")
    print(" ")

for i in range(altura):
    for j in range(altura-i):
        print(" * ",end = "")
    print(" ")