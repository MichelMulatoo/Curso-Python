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

# frutas = ('Naranja', 'Platano', 'Manzana')
# #Saber el largo
# print(frutas)
# print(len(frutas))
# # Acceder a un elemento
# print(frutas[0])
# #Navegacion inversa
# print(frutas[-1])
# #Acceder a un rango
# print(frutas[0:1])# sin incluir el ultimo indice
#
# #Recorrer elementos
# for fruta in frutas:
#     print(fruta, end=' ')
#
# #Cambiaar valor tupla
# frutaLista = list(frutas)
# frutaLista[0] = 'Pera'
# frutas = tuple(frutaLista)
# print('\n' ,frutas)# colocamos un salto de linea
#
# # eliminar una tupla por completo
# del frutas
# print(frutas)

#Crear una lista que solo incluya los numeros menores a 5
# tupla = (13, 1, 8, 3, 2, 5, 8)
#
# #define lista
# lista = []
#
# # se filtra los elementos menores a 5 de la tupla
# for elemento in tupla:
#     if elemento < 5:
#         lista.append(elemento)
# print(lista)


# Set

# planetas = {'Marte', 'Jupiter', 'Venus'}
# print(planetas)
#
# #Largo
# print(len(planetas))
# #Revisar si un elemento esta presente
# print('Marte' in planetas)
#
# # para agregar un elemento
# planetas.add('Tierra')
# print(planetas)
#
# #No se pueden duplicar los elementos
# planetas.add('Tierra')
# print(planetas)
#
# # eliminar elemento posiblemente arrojando un error
# planetas.remove('Tierra')
# print(planetas)
# #eliminar elemnto sin arrojar error
# planetas.discard('Jupiterre')
# print(planetas)
# # limpiar Set
# planetas.clear()
# print(planetas)
#
# #eliominar el set completo
# del planetas
# print(planetas)


# diccionario Python
# dict (Key, value)
diccionario = {

    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBM':'Database Management System'
}
print(diccionario)

#largo
print(len(diccionario))
# Acceder a un elemento (Key)
print(diccionario['IDE'])
#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# Modificamos elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

#Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprueba existencia de algun elemento
print('IDE' in diccionario)
# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#  Remover un elemento
diccionario.pop('DBM')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario
print(diccionario)

#Funcion es una bloque de codigo que se puede llamar una cantidad de veces














