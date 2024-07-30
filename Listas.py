

# una lista es un conjunto de elementos

nombres = ['Michel', 'Dayana,', 'Samy', 'Jhon']
#imprime una lista de nombre
print(nombres)
#accede a los elementos de manera inversa
print(nombres[0])

# accede a los elementos de manera inversa
print(nombres[-1])
#imprime un rango
print(nombres [0:2]) #sin incluir el indice 2
#ir del inicio de la lista al indice (isn incluirlo)
print(nombres[:3])
# desde el indice indicado hasta el final
print(nombres[1:])
nombres [3] = 'Mulato'
print(nombres)

#iterar las lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')
# pregunta el largo de una lista
print(len(nombres))

#agregar un elemento
nombres.append('Droguet')
print(nombres)