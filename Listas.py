#
#
# # una lista es un conjunto de elementos
#
# nombres = ['Michel', 'Dayana,', 'Samy', 'Jhon']
# #imprime una lista de nombre
# print(nombres)
# #accede a los elementos de manera inversa
# print(nombres[0])
#
# # accede a los elementos de manera inversa
# print(nombres[-1])
# #imprime un rango
# print(nombres [0:2]) #sin incluir el indice 2
# #ir del inicio de la lista al indice (isn incluirlo)
# print(nombres[:3])
# # desde el indice indicado hasta el final
# print(nombres[1:])
# nombres [3] = 'Mulato'
# print(nombres)
#
# #iterar las lista
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No existen mas nombres en la lista')
# # pregunta el largo de una lista
# print(len(nombres))
#
# #agregar un elemento
# nombres.append('Droguet')
# print(nombres)
# # insertar un elemento en un nindice especifico
# nombres.insert(1, 'Carrasco')
# print(nombres)
#
# #remover un elemento
# nombres.remove('Carrasco')
# print(nombres)
# # remover el ultimo valor agregado
# nombres.pop()
# print(nombres)
# #elimina un indice
# del nombres[0]
# print(nombres)
# #limpia la lista
# nombres.clear()
# print(nombres)
# #borrar la lista por completo
# del nombres
# print(nombres)


# # ejercicios 1 iterar un rango de 0 10 e imprimir numero divisibles entre 3
# print('Rango de 0 a 10 con munmero divisibles entre 3')
# for i in range(11):
#     if i % 3 == 0:
#         print(i)
#
# # ejercicios 2. Crear un rango de  numero de 2 a 6 e imprimir
# print('Rango con valores de inicio = 2 y fin = 6')
# rango = range(2,7)
# for i in rango:
#     print(i)
#
# # Ejercicio3 . Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
# print('Rango con valores de inicio = 3, fin = 10, incremento = 2 ')
# rango = range(3,11,2)
# for i in rango:
#     print(i)
#     print('Todo bien    ')


# Definir una tupla

frutas = ('Naranja', 'Platano', 'Manzana')
#Saber el largo
print(frutas)
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
#Navegacion inversa
print(frutas[-1])
#Acceder a un rango
print(frutas[0:1])

















